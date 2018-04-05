import time, sys
import json
import requests 
import http.client, urllib

dummy = '0'
var = 0
	
def notification():
	global dummy
	while True:
		url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
		response = urllib.request.urlopen(url)
		data = json.load(response)
		status = data['feeds'][0]['field1']
		entry = data['feeds'][0]['entry_id']
		if (status != dummy):
			dummy = status
			var = 1
			vadum = var+int(dummy)
			print ('Change')
			print (vadum)
			print (type(vadum))
			return vadum
		time.sleep(2)
		#print (status)
		#print (entry)