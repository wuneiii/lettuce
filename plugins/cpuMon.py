import os
import pickle

pluginInfo = {'name':'getSysInfo','version':'0.1'}
def reg():
	return {'interval':10 , 'enable':'disable'}

def client():
	info = os.uname()
	return {'data':'info' , 'msg': 'normal'}
	
