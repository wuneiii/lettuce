from util import web
from lettuce import webhd

urls = (
	'/', 'lettuce.webhd.dashboard',
)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
