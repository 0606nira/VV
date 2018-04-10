import time, sys
import json
import send
import requests 
import http.client, urllib


timeis = time.localtime()
timeat = time.strftime('%A %d %B %Y, %H:%M:%S', timeis) # กำหนดรูปแบบเวลา

dummy = 322

def notification():
        global i, light1_detect_int, dummy
        url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        entry_status = data['feeds'][1]['entry_id']
        be_status1 = data['feeds'][0]['field1']
        be_status2 = data['feeds'][0]['field2']
        last_status1 = data['feeds'][1]['field1']
        last_status2 = data['feeds'][1]['field2']
        if(entry_status != dummy):
                if(last_status1 != be_status1):
                        dummy = entry_status
                        light = 1
                        return last_status1, light
                else:
                        dummy = entry_status
                        light = 2
                        return last_status2, light
        else:
                pass
        print (entry_status)
		
