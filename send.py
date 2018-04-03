def send_values(light):
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
        print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())