import http.client, urllib
import time, sys

API_KEY_WRITE = 'WWRZDTPBUN0O18FM' #API สำหรับ ส่งค่า
API_KEY_READ = 'ZDDJL90IXYJOIQ3S' #API สำหรับ อ่านค่า
CHANNEL_ID = '455279'

def send_values(onoff):#ส่งค่าไฟห้องนอน 1คือเปิด 0คือปิด
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field1': onoff, 
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
		
	#ไฟห้องนอน : ปิด = 0 , เปิด = 1
	#ไฟห้องเก็บของ : ปิด = 2 , เปิด = 3
	#พัดลม : ปิด = 4 , เปิด = 5
	#ม่าน : ปิด = 6 , เปิด = 7
	#สปริงเกอร์ : ปิด = 8 , เปิด = 9
	