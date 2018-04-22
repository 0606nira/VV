import json
import time, sys, datetime
import requests
import http.client, urllib


def notification1(): #
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/1/last.json?api_key=5KWR29UNNEY0VV6W&result=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	last_status = data['field1'] #อ่านสถานะของอุปกรณ์
	return last_status
		
def notification2(): #
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/2/last.json?api_key=5KWR29UNNEY0VV6W&result=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	last_status = data['field2'] #อ่านสถานะของอุปกรณ์
	return last_status
			
def notification3(): #
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/3/last.json?api_key=5KWR29UNNEY0VV6W&result=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	last_status = data['field3'] #อ่านสถานะของอุปกรณ์
	return last_status
			
def notification4(): #
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/4/last.json?api_key=5KWR29UNNEY0VV6W&result=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	last_status = data['field4'] #อ่านสถานะของอุปกรณ์
	return last_status

def notification5(): #
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/472273/fields/5/last.json?api_key=5KWR29UNNEY0VV6W&result=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	last_status = data['field5'] #อ่านสถานะของอุปกรณ์
	return last_status

	
					
