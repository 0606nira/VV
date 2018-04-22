import json
import time, sys, datetime
import requests
import http.client, urllib.request


def weather():
	message = event.message.text
	url = 'http://data.tmd.go.th/api/WeatherToday/V1/?type=json'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	lastbuild = data['Header']['LastBuiltDate']
	print(lastbuild)
	station = input("Specify Station Name: ")
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text=station))
		
	#message = event.message.text
	a = data['Stations']
	i = 0
	while i < len(a):
		c = a[i]
		c1 = c['Observe']
		Temp = c1['Temperature']['Value']
		Max_Temp = c1['MaxTemperature']['Value']
		Min_temp = c1['MinTemperature']['Value']
		staname = c['StationNameTh']
		#print (staname.find(station))
		if(staname.find(message) >= 0):
			print("""Temp is '{0}'.
Max Temp is '{1}'.
Min Temp is '{2}'.
at '{3}'.""".format(Temp, Max_Temp, Min_temp, lastbuild))
			line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text="""Temp is '{0}'.
Max Temp is '{1}'.
Min Temp is '{2}'.
at '{3}'.""".format(Temp, Max_Temp, Min_temp, lastbuild)))
			break
		else:
			i += 1
				