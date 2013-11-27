import os
import socket
import json
import select
import threading
from lettuce import data as dm
from util import log

class Server(object):
	def __init__(self, config):
		self.config = config
		self.serverAddr = (config['server_ip'], int(config['server_port']))
		self.socket = None
		self.aliveClient = {}
	def startServer(self):
		sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
		sock.setblocking(False)
		sock.bind(self.serverAddr)
		sock.listen(1)
	
		while True:
			rs,ws,es = select.select([sock] , [] , [sock])
			for s in rs:
				if s is sock:
					conn,addr = s.accept()
					print 'connect by' + str(addr)
					#log.getLogger().info('connect by ' + str(addr))
					self.newThreadWorker(conn)
				else:
					print ' sock in ws'
			for s in es:
				print 'except',s.getpeername()
				s.close();
	
	def newThreadWorker(self,conn):
		#print 'new Thread Workder ' + str(conn.fileno())
		worker = threading.Thread(target=self.t,args = [conn] )
		worker.start()
	def t(self,conn):
		data = conn.recv(1024)
		conn.close()
	
		args = json.loads(data)
		if args['plugin'] == 'watchDog' : 
			self.aliveClient[args['client_name']] = args['ts']
			dm.regClient(args['client_name'])
			if not os.path.exists('./data/' + args['client_name']):	
				os.mkdir('./data/' + args['client_name'])
		else:
			pass
