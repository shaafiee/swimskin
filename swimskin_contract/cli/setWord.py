#from sha3 import keccak_256
from web3 import Web3
#import rlp
import json
import sys
import re
import psycopg2
import time
import os
import random
import sha3
#from array import array
#import numpy
sys.path.append('/root/dunghole/eth_py/lib')
#from endpoint import getLocalEndpoint
from endpoint import getRopstenEndpoint

from pcake import getEthValue
from pcake import getTokenValue

sys.path.append('/root/nftwordle/cli')
from ethAddress import *

#w3 = Web3(Web3.HTTPProvider('http://67.227.137.10:16501'))
#w3 = Web3(Web3.HTTPProvider(getLocalEndpoint()))
w3 = Web3(Web3.HTTPProvider(getRopstenEndpoint()))
conn = psycopg2.connect(host="127.0.0.1", port="54341", database="ethereum", user="postgres", password="fanif@x3R")
cur = conn.cursor()


#ethAddress = '0x56B61C313e68A0a0354368616e0c100BC046a59d'


#fromAddress = '0x8cEDf25d0E6Da494b2268BA8ef6a65734906AC68'
fromAddress = '0x488822a0128dE0f931543563E859742270A22105'
contracts = {"init":0}
decimals = {"init":0}

contract_abi = None
with open('/root/nftwordle/cli/NFTWordle.json') as f:
	contract_abi = json.load(f)

from contract import checkContract

def updateContracts():
	currentBlock = w3.eth.blockNumber
	nonce = w3.eth.getTransactionCount(fromAddress)
	appContract = w3.eth.contract(address=ethAddress, abi=contract_abi)
	#transaction = appContract.functions.setNewWordle(endLetters0, endLetters1, endLetters2, endLetters3, endLetters4).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	currentDay = appContract.functions.currentDay().call()
	currentRound = appContract.functions.currentRound().call()

	resetDay = False
	roundWinners = appContract.functions.roundWinners(currentDay, currentRound).call()
	cur.execute("select * from nwd_dayshift")
	if cur.rowcount > 0 or currentRound == 0:
		cur.execute("delete from nwd_dayshift")
		resetDay = True
	print("round winners", roundWinners, currentDay, currentRound)

	t2 = 1
	t3 = 1
	t4 = 1
	t5 = 1
	t6 = 1
	hashAlreadySet = False
	if currentRound == 0:
		t6 = random.randint(1, 10000)
		t3 = random.randint(10001, 20000)
		t2 = random.randint(20001, 30000)
		t5 = random.randint(30001, 40000)
		t4 = random.randint(40001, 50000)
		cDay = 1
		cur.execute("insert into nwd_hashes (day, t2, t3, t4, t5, t6) values (%s, %s, %s, %s, %s, %s)", [cDay, t2, t3, t4, t5, t6])
		conn.commit()
		hashAlreadySet = True
	else:
		#cur.execute("insert into nwd_hashes (day, t2, t3, t4, t5, t6) values (%s, %s, %s, %s, %s, %s)", [cDay, t2, t3, t4, t5, t6])
		cur.execute("select t2, t3, t4, t5, t6 from nwd_hashes where day = " + str(currentDay))
		if cur.rowcount > 0:
			t2, t3, t4, t5, t6 = list(cur.fetchone())

	
	#resetDay = True
	if roundWinners < 30 and not resetDay:
		return

	cur.execute("select salt from wordlesalt")
	currentHash = 0
	currentSalt = 12
	if cur.rowcount > 0:
		currentSalt = cur.fetchone()[0]
	k = sha3.keccak_256()
	letterNow = str(currentSalt)
	encoded = letterNow.encode('utf-8')
	k.update(encoded)
	currentHash = int(k.hexdigest(), 16)

	cur.execute("select count(word) from words")
	wordTotal = cur.fetchone()[0]

	cur.execute("select min(id), max(id) from words where category = 1")
	minId, maxId = list(cur.fetchone())


	wordIdx = random.randint(1, (maxId - minId))
	wordIdx = wordIdx + minId

	cur.execute("select word from words where id = " + str(wordIdx))
	word = cur.fetchone()[0]
	rndNo = random.randint(1, 60000)
	cur.execute("delete from wordlesalt")
	conn.commit()
	cur.execute("insert into wordlesalt (salt, word_id) values (" + str(rndNo) + ", " + str(wordIdx) +  ")")
	conn.commit()

	saltashes = []
	currentKeys = [t2, t3, t4, t5, t6]

	k = sha3.keccak_256()
	letterNow = str(currentKeys[0])
	encoded = letterNow.encode('utf-8')
	k.update(encoded)
	saltashes.append(int(k.hexdigest(), 16))

	k = sha3.keccak_256()
	letterNow = str(currentKeys[1])
	encoded = letterNow.encode('utf-8')
	k.update(encoded)
	saltashes.append(int(k.hexdigest(), 16))

	k = sha3.keccak_256()
	letterNow = str(currentKeys[2])
	encoded = letterNow.encode('utf-8')
	k.update(encoded)
	saltashes.append(int(k.hexdigest(), 16))

	k = sha3.keccak_256()
	letterNow = str(currentKeys[3])
	encoded = letterNow.encode('utf-8')
	k.update(encoded)
	saltashes.append(int(k.hexdigest(), 16))

	k = sha3.keccak_256()
	letterNow = str(currentKeys[4])
	encoded = letterNow.encode('utf-8')
	k.update(encoded)
	saltashes.append(int(k.hexdigest(), 16))



	#encLetters = [sha3.keccak_256(ord(letters[0]) + rndNo), sha3.keccak_256(ord(letters[1]) + rndNo), sha3.keccak_256(ord(letters[2]) + rndNo), sha3.keccak_256(ord(letters[3]) + rndNo), sha3.keccak_256(ord(letters[4]) + rndNo)]
	print(roundWinners, currentDay, currentRound)
	#return


	#transaction = appContract.functions.setNewWordle(appContract.encodeABI(fn_name="setNewWordle", args=[endLetters])).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	gasPrice = w3.eth.gasPrice
	transaction = appContract.functions.newRound(currentKeys, resetDay).buildTransaction({'gas':500000,'gasPrice':gasPrice,'from':fromAddress,'nonce':nonce})
	#privateKey='0x16553f520b12ad99d68c492f6968d97c5f5beecf928508006d2d907532641754'
	#privateKey='0x6c859fadd3e5c5784c95eb62cd967685b71fc1c60d71664493b59feb09585a6f'
	privateKey='0x6c859fadd3e5c5784c95eb62cd967685b71fc1c60d71664493b59feb09585a6f'
	signedTxn = w3.eth.account.signTransaction(transaction, private_key=privateKey)
	w3.eth.sendRawTransaction(signedTxn.rawTransaction)

	#supply = appContract.functions.totalSupply().call()
	
	if resetDay and not hashAlreadySet:
			t6 = random.randint(1, 10000)
			t3 = random.randint(10001, 20000)
			t2 = random.randint(20001, 30000)
			t5 = random.randint(30001, 40000)
			t4 = random.randint(40001, 50000)
			cDay = currentDay + 1
			cur.execute("insert into nwd_hashes (day, t2, t3, t4, t5, t6) values (%s, %s, %s, %s, %s, %s)", [cDay, t2, t3, t4, t5, t6])
			conn.commit()


if __name__ == '__main__':
	updateContracts()

