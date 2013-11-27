import socket,time
from util import linuxInfo

def clientToServer(socket, msg):
	body = {'id':linuxInfo.getSelfIp() , 'ts' :time.time(), 'data':msg}
	socket.sendall(body)
	
