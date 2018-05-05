import http.client, urllib
import time, sys

API_KEY_WRITE = 'E34W34GC4JCO4K3R' #API สำหรับ ส่งค่า Channel Home status
API_KEY_READ = '5KWR29UNNEY0VV6W' #API สำหรับ อ่านค่า
CHANNEL_ID = '472273'

def send_values1(sta_1):#ส่งค่าไฟห้องนอน 0 =ปิด, 1 =เปิด, 2=อัตโนมัติ 
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field1': sta_1, 
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
		

def send_values2(sta_2):#ส่งค่าไฟห้องเก็บของ 0 =ปิด, 1 =เปิด, 2=อัตโนมัติ 
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field2': sta_2, 
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
		
def send_values3(sta_3):#ส่งค่าพัดลม 0 =ปิด, 1 =เปิด, 2=อัตโนมัติ 
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field3': sta_3, 
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
		
def send_values4(sta_4):#ส่งค่าหน้าต่าง 0 =ปิด, 1 =เปิด, 2=อัตโนมัติ 
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field4': sta_4, 
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
		
def send_values5(sta_5):#ส่งค่าสปริงเกอร์ 0 =ปิด, 1 =เปิด, 2=อัตโนมัติ 
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field5': sta_5, 
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