import json
import time, sys, datetime
import http.client, urllib

def notification1():
	global dummy #ตั้งเป็นตัวแปรหลอก
	print ('dummy: ', dummy)
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/1/last.json?api_key=5KWR29UNNEY0VV6W&result=2'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][1]['entry_id']
	print ('entry_status: ', entry_status)
	last_status = data['feeds'][1]['field1'] #อ่านสถานะของอุปกรณ์
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status != None):
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			print ('dummy1: ', dummy)
			return last_status
		
def notification2():
	global dummy #ตั้งเป็นตัวแปรหลอก
	print ('dummy: ', dummy)
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/2/last.json?api_key=5KWR29UNNEY0VV6W&result=2'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][1]['entry_id']
	print ('entry_status: ', entry_status)
	last_status = data['feeds'][1]['field1'] #อ่านสถานะของอุปกรณ์
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status != None):
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			print ('dummy1: ', dummy)
			return last_status
			
def notification3():
	global dummy #ตั้งเป็นตัวแปรหลอก
	print ('dummy: ', dummy)
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/3/last.json?api_key=5KWR29UNNEY0VV6W&result=2'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][1]['entry_id']
	print ('entry_status: ', entry_status)
	last_status = data['feeds'][1]['field1'] #อ่านสถานะของอุปกรณ์
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status != None):
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			print ('dummy1: ', dummy)
			return last_status
			
def notification4():
	global dummy #ตั้งเป็นตัวแปรหลอก
	print ('dummy: ', dummy)
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/4/last.json?api_key=5KWR29UNNEY0VV6W&result=2'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][1]['entry_id']
	print ('entry_status: ', entry_status)
	last_status = data['feeds'][1]['field1'] #อ่านสถานะของอุปกรณ์
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status != None):
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			print ('dummy1: ', dummy)
			return last_status

def notification5():
	global dummy #ตั้งเป็นตัวแปรหลอก
	print ('dummy: ', dummy)
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/5/last.json?api_key=5KWR29UNNEY0VV6W&result=2'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][1]['entry_id']
	print ('entry_status: ', entry_status)
	last_status = data['feeds'][1]['field1'] #อ่านสถานะของอุปกรณ์
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status != None):
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			print ('dummy1: ', dummy)
			return last_status