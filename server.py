from lettuce import server
from util import config

config = config.loadConfig('./config/server.conf');
server = server.Server(config);
server.startServer();
