import os

def loadConfig(file):
	data = {}
	if not os.path.exists(file):
		return False
	fd = open(file)
	config = fd.readlines()
	for option in config:
		[key,value] = option.split('=')
		data[key.strip()] = value.strip()
	return data

