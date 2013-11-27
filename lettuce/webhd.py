from util import web
from util import date
from lettuce import data

render = web.template.render('assets/template/')

class index:
	def GET(self):
		return 'index'


class dashboard:
	def GET(self):
		client_data  = []
		all_client = data.getAllClient()
		for client in all_client:
			client_data.append({'name': client , 'reg_time' : date.t(all_client[client])})
		
		return render.list_client(client_data)
		

