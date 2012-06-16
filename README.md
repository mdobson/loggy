Loggy: The simple way to roll your own heroku logging solution
==============================================================

##Overview##

This is a simple log access utility born out of a need to access raw logs on my heroku app. Input your API key and deploy to have contant log feed. Or post your API key and app name as GET arguments in that order to get your log feed.


Three simple steps for this app:

1. Clone this repo
2. Create an application on heroku
3. Push!

Then have your browser or other consumers issue a GET request to that url with two other URL parameters like so.

logs.yoursite.com/?q=YOUR_API_KEY&?t=YOUR_APP_NAME

Then you'll get your logs in a nicely formatted JSON stream. 

##Stream Format##

The stream is just a simple javascript array of JSON objects:
```json
{
	date : "is the date the log was recorded on",
	process : "is the process that was being logged (Typically either your application or heroku internals for routing)",
	message : "is the message that was logged by the particular process',
	time : "is the time the log was recorded on"
}
```
##The Long Run##

For now I'll keep building on this if I need new features. If you've forked, and think there is a good feature that belongs in core issue a pull request and we can figure it out :)

## License ##

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
