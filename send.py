import http.client, urllib
import time, sys

API_KEY_WRITE = 'WWRZDTPBUN0O18FM'
API_KEY_READ = 'ZDDJL90IXYJOIQ3S'
CHANNEL_ID = '455279'

def send_values1(light):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field1': light, 
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        #print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            #print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())
		
def send_values2(light):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field2': light,
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        #print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            #print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())
		
def send_values3(fan):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field3': fan, 
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        #print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            #print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())
		
def send_values4(curtain):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field4': curtain, 
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        #print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            #print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())
		
def send_values5(springer):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field5': springer, 
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        #print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            #print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())