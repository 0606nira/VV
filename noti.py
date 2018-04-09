import time, sys
import json
import send
import requests 
import http.client, urllib


timeis = time.localtime()
timeat = time.strftime('%A %d %B %Y, %H:%M:%S', timeis) # กำหนดรูปแบบเวลา

dummy = 315

def notification():
        global dummy
        url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        entry_status = data['feeds'][1]['entry_id']
        status = data['feeds'][1]['field1']
        if(entry_status == dummy + 1):
			dummy = int(entry_status)
			return status
        else:
			pass
        print (dummy)
        print (entry_status)
		
