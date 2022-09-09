#from sha3 import keccak_256
import psycopg2

#w3 = Web3(Web3.HTTPProvider('http://67.227.137.10:16501'))
#w3 = Web3(Web3.HTTPProvider(getLocalEndpoint()))
conn = psycopg2.connect(host="127.0.0.1", port="54341", database="ethereum", user="postgres", password="fanif@x3R")
cur = conn.cursor()



def updateContracts():
	cur.execute("insert into nwd_dayshift (shiftnow) values ('t')")
	conn.commit()


if __name__ == '__main__':
	updateContracts()

