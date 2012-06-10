import heroku
import json
import tornado.ioloop
import tornado.web
import os

def initialize_heroku():
	cloud = heroku.from_key("INSERT_KEY_HERE")
	app = cloud.apps["INSERT_APP_NAME_HERE"]
	return app

def get_data():
	app = initialize_heroku()
	logs = app.logs()
	listOfSplitLogs = logs.split('\n')
	listOfParsedLogs = []
	for line in listOfSplitLogs:
		 listOfParsedLogs.append(line.split(' '))
	listOfDicts = []
	for line in listOfParsedLogs:
		if len(line) > 2:
			dictionary = {}
			dateAndTime = line[0].split("T")
			process = line[1]
			message = " ".join(line[2:])
			dictionary['date'] = dateAndTime[0]
			dictionary['time'] = dateAndTime[1]
			dictionary['process'] = process
			dictionary['message'] = message
			listOfDicts.append(dictionary)
	return json.dumps(listOfDicts)

def stream_data():
	app = initialize_heroku()
	logs = app.logs(tail=True)
	for line in logs:
		print line

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "application/json")
		self.write(get_data())


application = tornado.web.Application([
	(r"/", MainHandler),
])

def start():
	if __name__ == "__main__":
		application.listen(os.environ.get("PORT", 5000))
		tornado.ioloop.IOLoop.instance().start()

start()