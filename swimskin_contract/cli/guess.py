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
	#transaction = appContract.functions.setNewWordle(endLetters0, endLetters1, endLetters2, endLetters3, endLetters4).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	#transaction = appContract.functions.setNewWordle(appContract.encodeABI(fn_name="setNewWordle", args=[endLetters])).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	#transaction = appContract.functions.guess([100679515309546144113367463904342228835072462283035494618084836237367450270639, 35897045882788569693861594843998381973907197822570853752185082880124771581579, 85300552420282404761841164481130111650376345869375316370362014748065614287873, 50509056941842860508543703927355855048473514863397224817703459635579649390118, 10997807724885742435620451868093000077625004675432265889779048586475688056202]).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	transaction = appContract.functions.guess([100679515309546144113367463904342228835072462283035494618084836237367450270639]).buildTransaction({'gas':200000,'gasPrice':w3.toWei('120','gwei'),'from':fromAddress,'nonce':nonce})
	privateKey='0x16553f520b12ad99d68c492f6968d97c5f5beecf928508006d2d907532641754'
	signedTxn = w3.eth.account.signTransaction(transaction, private_key=privateKey)
	w3.eth.sendRawTransaction(signedTxn.rawTransaction)

	#supply = appContract.functions.totalSupply().call()
	


if __name__ == '__main__':
	updateContracts()

