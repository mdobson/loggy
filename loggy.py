"""
    Copyright (C) 2012  Matthew Dobson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import heroku
import json
import tornado.ioloop
import tornado.web
import os

def initialize_heroku():
	cloud = heroku.from_key("INSERT_KEY_HERE")
	app = cloud.apps["APP_NAME_HERE"]
	return app

def get_data(api, app):
	#app = initialize_heroku()
	cloud = heroku.from_key(api)
	app = cloud.apps[app]
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
		queryParams = self.request.uri[2:]
		queries = queryParams.split('&')
		apiKey = queries[0].split('=')[1]
		appName = queries[1].split('=')[1]
		if(apiKey and appName):
			self.write(get_data(apiKey, appName))
		else:
			self.write("Failed")
		#self.write(get_data())


application = tornado.web.Application([
	(r"/", MainHandler),
])

def start():
	if __name__ == "__main__":
		application.listen(os.environ.get("PORT", 5000))
		tornado.ioloop.IOLoop.instance().start()

start()