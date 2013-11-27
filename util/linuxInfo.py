import os,socket
def diskInfo():
	data = {}
	f = open("/proc/mounts")
	lines = f.readlines()
	for line in lines:
		sline = line.split(' ')
		mountPoint = sline[0]
		data[mountPoint] = {'mount': sline[1],'type': sline[2] ,'proto': sline[3]}
		if os.path.exists(mountPoint):
			hddinfo = os.statvfs(mountPoint)
			data[mountPoint]['total'] = hddinfo.f_frsize * hddinfo.f_blocks
    			data[mountPoint]['free'] = hddinfo.f_frsize * hddinfo.f_bavail
    			data[mountPoint]['used']= hddinfo.f_frsize * (hddinfo.f_blocks - hddinfo.f_bfree)
			 
	return data
def memInfo():
	pass

def cpuInfo():
	pass

def netInfo():
	pass
def getSelfIp():
	ip = socket.gethostbyname(socket.gethostname())
	return ip
def getHostName():
	return socket.gethostname()
	
print getHostName();
