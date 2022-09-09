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

from eth_account import Account
import secrets
import re

#w3 = Web3(Web3.HTTPProvider('http://67.227.137.10:16501'))
#w3 = Web3(Web3.HTTPProvider(getLocalEndpoint()))
w3 = Web3(Web3.HTTPProvider(getRopstenEndpoint()))
conn = psycopg2.connect(host="127.0.0.1", port="54341", database="ethereum", user="postgres", password="fanif@x3R")
cur = conn.cursor()


#ethAddress = '0x56B61C313e68A0a0354368616e0c100BC046a59d'


#fromAddress = '0x8cEDf25d0E6Da494b2268BA8ef6a65734906AC68'
fromAddress ='0x488822a0128dE0f931543563E859742270A22105'

contracts = {"init":0}
decimals = {"init":0}

contract_abi = None
with open('NFTWordle.json') as f:
	contract_abi = json.load(f)

from contract import checkContract

def updateContracts():
	accounts = []
	f = open("wl1.csv", "w")
	for row in open('wl.csv'):
		row.strip()
		row.lstrip()
		row = re.sub("\s*","",row)
		accounts.append(Web3.toChecksumAddress(row))
		
	f.close()

	print(accounts)
#	for i in range(0, 100):
#		priv = secrets.token_hex(32)
#		private_key = "0x" + priv
#		#print ("SAVE BUT DO NOT SHARE THIS:", private_key)
#		acct = Account.from_key(private_key)
#		accounts.append(acct.address)
#		print("Address:", accounts[i])
#
	#rounds = appContract.functions.saleIsActive().call()
	#rounds = appContract.functions.currentDay().call()
	#print(rounds)


if __name__ == '__main__':
	updateContracts()

