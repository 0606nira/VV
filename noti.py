import time, sys
import json
import requests 
import http.client, urllib

API_KEY_WRITE = 'WWRZDTPBUN0O18FM'
API_KEY_READ = 'ZDDJL90IXYJOIQ3S'
CHANNEL_ID = '455279'
	
def notification():
	while True:
        global API_KEY_READ
        url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        status = data['feeds'][0]['field1']
        sta = data['feeds'][1]['field1']
		if(status == 1):
			line_bot_api.push_message(
				event.source.user_id or event.source.group_id or event.source.room_id, 
				TextSendMessage(text='Light On'))
		time.sleep(5)
		#print (status)
		#print (sta)
		