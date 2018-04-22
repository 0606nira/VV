import json
import time, sys, datetime
import requests
import http.client, urllib.request


def weather(city):
	url = 'http://data.tmd.go.th/api/WeatherToday/V1/?type=json'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	lastbuild = data['Header']['LastBuiltDate']
	name = city
	a = data['Stations']
	i = 0
	while i < len(a):
		c = a[i]
		c1 = c['Observe']
		Temp = c1['Temperature']['Value']
		Max_Temp = c1['MaxTemperature']['Value']
		Min_temp = c1['MinTemperature']['Value']
		stanameth = c['StationNameTh']
		stanameen = c['StationNameEng']
		#print (staname.find(station))
		if(stanameen == name):
			ans = """Station's Name is '{4}'
Temp is '{0}'.
Max Temp is '{1}'.
Min Temp is '{2}'.
at '{3}'.""".format(Temp, Max_Temp, Min_temp, lastbuild, stanameth)
			return ans
			break
		else:
			i += 1
