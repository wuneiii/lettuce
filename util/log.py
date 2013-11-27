import logging
import os

def getLogger():
	#logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s')  
	logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
	return logging
	
