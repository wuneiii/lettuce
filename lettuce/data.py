import os
import json
import time

dataDir = './data/'
regFile = dataDir + 'client_list.dat'

def getContent(filePath):
	fd = open(filePath , 'r+')
	content = fd.read()
	fd.close()
	return content

def putContent(filePath, data):
	fd = open(filePath , 'w')
	fd.write(data)
	fd.close()

def regClient(clientName):
	data = getContent(regFile)
	if len(data) == 0:
		data = {}
	else:
		data = json.loads(data)
	data[clientName] = time.time()
	putContent(regFile , json.dumps(data))
def getAllClient():
	data = getContent(regFile)
	return json.loads(data)
