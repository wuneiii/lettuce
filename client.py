#!/usr/bin/python
import os,sys
from util import config
from lettuce import client

configFile = 'config/client.conf'
config = config.loadConfig(configFile)

client = client.Client(config)
client.startClient()

