import json
import time, sys, datetime
import http.client, urllib

timeis = time.localtime()
timeat = time.strftime('%A %d %B %Y, %H:%M:%S', timeis) # กำหนดรูปแบบเวลา

def detail_temp():
	url = 'https://api.thingspeak.com/channels/455279/fields/1/last.json?api_key=ZDDJL90IXYJOIQ3S'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['entry_id']
	print ('entry_status: ', entry_status)
	last_temp = data['field1']
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text="Temp. is '{0}' check at '{1}'".format(last_temp, timeat)))

def detail_humi():
	url = 'https://api.thingspeak.com/channels/455279/fields/2/last.json?api_key=ZDDJL90IXYJOIQ3S'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['entry_id']
	print ('entry_status: ', entry_status)
	last_humi = data['field2']
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text="Humidity is '{0}' check at '{1}'".format(last_humi, timeat))

def detail_lux():
	url = 'https://api.thingspeak.com/channels/455279/fields/4/last.json?api_key=ZDDJL90IXYJOIQ3S'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['entry_id']
	print ('entry_status: ', entry_status)
	last_lux = data['field3']
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text="LUX is '{0}' check at '{1}'".format(last_lux, timeat)))		