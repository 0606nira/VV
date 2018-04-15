import json
import time, sys, datetime
import http.client, urllib

API_KEY_WRITE = 'E34W34GC4JCO4K3R'

def mode(Mode):
	global API_KEY_WRITE
	params = urllib.parse.urlencode(
		{'field1': Mode, 
		'key': API_KEY_WRITE} )
	headers = { "Content-Type": "application/x-www-form-urlencoded",
		"Accept": "text/plain" }
	conn = http.client.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request( "POST", "/update", params, headers ) # send HTTP request
		resp = conn.getresponse() # get HTTP response
		#print ('status:', resp.status, resp.reason) # read HTTP status
		entry_id = resp.read()  # read response string
		field1 = resp.read()
		conn.close()            # close HTTP connection
		if entry_id.isdigit() and int(entry_id) > 0:
			print ('Entry ID:', entry_id)
			print ('mode is: ', fielse1)
			return True
		else:
			return False
	except:
		print ("connection failed", sys.exc_info())

			#mode auto = 1
			#mode manual = 0