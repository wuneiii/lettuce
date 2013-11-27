import socket
import select
import time
import Queue
import sched
import threading
import json


from lettuce import netMessage
from lettuce import plugin
from util import linuxInfo
class Client(object):
	def __init__(self,config):
		self.config = config
		self.serverAddr = (config['server_ip'], int(config['server_port']))

		self.pluginInfo = {}
		self.sched = sched.scheduler(time.time,time.sleep)
	def startClient(self):
		
		allPlugin = plugin.getPluginList()
		for plug in allPlugin:
			pinfo = plugin.getRegInfo(plug)
			if pinfo.has_key('enable') and pinfo['enable'] == 'disable':
				continue;
			self.pluginInfo[plug] = pinfo
			self.registerSched(plug)
		self.sched.run()
		print 'over'
	def execPlugin(self, pluginName, argv = ()):
		self.registerSched(pluginName)
		newThread = threading.Thread(target=self.taskThread , args=[pluginName])	
		newThread.start()
		
		print 'already start thread for plugin :  '+  pluginName
	
	def registerSched(self,plugin):
		self.sched.enter(self.pluginInfo[plugin]['interval'] ,1 ,self.execPlugin,(plugin,()))
		#print 'plugin ' + plugin +' will exec after ' + str(self.pluginInfo[plugin]['interval'])
	def taskThread(self, pluginName):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(self.serverAddr)
		plugModule = __import__(pluginName)
		ret = plugModule.client()
		ret['ts'] = time.time()
		ret['plugin'] = pluginName
		ret['client_name'] = self.getClientName()
		sock.sendall(json.dumps(ret))
		sock.close()
	def getClientName(self):
		if self.config['client_name'] == '' or self.config.has_key('client_name'):
			return linuxInfo.getHostName()
		else:
			return self.config['client_name']
