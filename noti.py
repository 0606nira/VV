import time, sys
import json
import requests 
import http.client, urllib
	
def notification():
	url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
	response = urllib.request.urlopen(url)
	data = json.load(response)
	status = data['feeds'][0]['field1']
	#sta = data['feeds'][1]['field1']
	return status
	#print (status)
	#print (sta)	