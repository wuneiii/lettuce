import time

def t(ts):
	return time.strftime('%Y-%m-%d %H:%M:%S' , time.gmtime(ts))


print t(1385451672.04566)
