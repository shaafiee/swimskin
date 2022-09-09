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


#fromAddress = '0x8cEDf25d0E6Da494b2268BA8ef6a65734906AC68'
fromAddress = '0x488822a0128dE0f931543563E859742270A22105'
contracts = {"init":0}
decimals = {"init":0}

contract_abi = None
with open('NFTWordle.json') as f:
	contract_abi = json.load(f)

from contract import checkContract

def updateContracts():

	currentBlock = w3.eth.blockNumber
	nonce = w3.eth.getTransactionCount(fromAddress)
	gasPrice = w3.eth.generate_gas_price()
	print(gasPrice)
	appContract = w3.eth.contract(address=ethAddress, abi=contract_abi)
	#transaction = appContract.functions.setNewWordle(endLetters0, endLetters1, endLetters2, endLetters3, endLetters4).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	#transaction = appContract.functions.setNewWordle(appContract.encodeABI(fn_name="setNewWordle", args=[endLetters])).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	gasPrice = w3.eth.gasPrice
	print(gasPrice)
	transaction = appContract.functions.setBaseURI('QmYHBzvzhs5YKvJVav2NzpxyxVJe2ygtW3JQeTmWJrEwZs').buildTransaction({'gas':50000,'gasPrice':w3.toWei('200','gwei'),'from':fromAddress,'nonce':nonce})
	#privateKey='0x16553f520b12ad99d68c492f6968d97c5f5beecf928508006d2d907532641754'
	privateKey='0x6c859fadd3e5c5784c95eb62cd967685b71fc1c60d71664493b59feb09585a6f'
	signedTxn = w3.eth.account.signTransaction(transaction, private_key=privateKey)
	w3.eth.sendRawTransaction(signedTxn.rawTransaction)

	#supply = appContract.functions.totalSupply().call()
	


if __name__ == '__main__':
	updateContracts()

