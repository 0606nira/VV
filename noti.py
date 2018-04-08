import time, sys
import json
import requests 
import http.client, urllib
	
def notification():
    while True:
        url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        sta = data['feeds'][0]['field1']
        #entry_sta = data['feeds'][0]['entry_id']
        status = data['feeds'][1]['field1']
        #entry_status = data['feeds'][1]['entry_id']
        dummy = 0
        if(status != sta):
            if(status == '1'):
                send_values1(1)
                dummy = 'On'
                #print (dummy)
                return dummy
            elif(status == '0'):
                send_values1(0)
                dummy = 'Off'
                #print (dummy)
                #print (status)
                return dummy
        print (dummy)
        time.sleep(10)
        #print (status)
        #print (sta)