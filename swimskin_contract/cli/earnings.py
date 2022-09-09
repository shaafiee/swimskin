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

from ethAddress import *

#w3 = Web3(Web3.HTTPProvider('http://67.227.137.10:16501'))
#w3 = Web3(Web3.HTTPProvider(getLocalEndpoint()))
w3 = Web3(Web3.HTTPProvider(getRopstenEndpoint()))
conn = psycopg2.connect(host="127.0.0.1", port="54341", database="ethereum", user="postgres", password="fanif@x3R")
cur = conn.cursor()


#ethAddress = '0x56B61C313e68A0a0354368616e0c100BC046a59d'


fromAddress = '0x8cEDf25d0E6Da494b2268BA8ef6a65734906AC68'

contracts = {"init":0}
decimals = {"init":0}

contract_abi = None
with open('NFTWordle.json') as f:
	contract_abi = json.load(f)

from contract import checkContract

def updateContracts():

	currentBlock = w3.eth.blockNumber
	nonce = w3.eth.getTransactionCount(fromAddress)
	appContract = w3.eth.contract(address=ethAddress, abi=contract_abi)
	#transaction = appContract.functions.buyRounds().buildTransaction({'value':w3.toWei('0.01','ether'),'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	#privateKey='0x16553f520b12ad99d68c492f6968d97c5f5beecf928508006d2d907532641754'
	#signedTxn = w3.eth.account.signTransaction(transaction, private_key=privateKey)
	#w3.eth.sendRawTransaction(signedTxn.rawTransaction)

	rounds = appContract.functions.winner(28455, 3, '0xa0f2D9F342D43306D16F1b6c35Ff886BA50f809a').call()
	print(rounds)
	rounds = appContract.functions.currentRound().call()
	#rounds = appContract.functions.currentDay().call()
	print(rounds)


if __name__ == '__main__':
	updateContracts()

