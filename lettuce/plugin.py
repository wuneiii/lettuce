import os,sys,time
from util import linuxInfo


pluginDir = os.path.realpath('./plugins/')
def getPluginName(file):
	return os.path.basename(file)
	

def getPluginList():
	plugins = []
	pluginList = os.listdir(pluginDir)
	for p in pluginList:
       		if p.endswith('.py') and (p != '__init__.py') :
			plugins.append(p[0:-3])
	return plugins

	
def getRegInfo(pluginName):
	sys.path.append(pluginDir)
	plugModule = __import__(pluginName)
	return plugModule.reg()
