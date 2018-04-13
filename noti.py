import time, sys, datetime
import json
import send
import requests 
import http.client, urllib


dummy = 0

def notification():
	global dummy #ตั้งเป็นตัวแปรหลอก
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][0]['entry_id']
	last_status_light1 = data['feeds'][0]['field1'] #สถานะไฟล่าสุดในห้องนอน
	last_status_light2 = data['feeds'][0]['field2'] #สถานะไฟล่าสุดในห้องเก็บของ
	last_status_fan = data['feeds'][0]['field3']
	last_status_curtain = data['feeds'][0]['field4']
	last_status_springer = data['feeds'][0]['field5']
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status_light1 is not None): 
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			light = 1
			return last_status_light1, light #คืนค่ากลับ บอกสถานะไฟและห้องที่มีการเปลี่ยนแปลง
		if(last_status_light2 is not None):
			dummy = entry_status
			light = 2
			return last_status_light2, light
		if(last_status_fan is not None):
			dummy = entry_status
			fan = 3
			return last_status_fan, fan
		if(last_status_curtain is not None):
			dummy = entry_status
			curtain = 4
			return last_status_curtain, curtain
		if(last_status_springer is not None):
			dummy = entry_status
			springer = 5
			return last_status_springer, springer
		
