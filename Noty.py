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

def monitor():
        #g = ['LED Bedroom', 'LED Stroageroom', 'Fan', 'Curtain', 'Springer']
        l = ['Off', 'On', 'Sensor Mode']
        j = 0
        nl = '\n'
        while(j <= 2):
                        if(notification1() == str(j)):
                                ans1 = "LED Bedroom's status is {0}".format(l[j])
                                #print (ans1)
                        if(notification2() == str(j)):
                                ans2 = "LED Garage's status is {0}".format(l[j])
                                #print (ans2)
                        if(notification3() == str(j)):
                                ans3 = "Fan's status is {0}".format(l[j])
                                #print (ans3)
                        if(notification4() == str(j)):
                                ans4 = "Window's status is {0}".format(l[j])
                                #print (ans4)
                        if(notification5() == str(j)):
                                ans5 = "Springer's status is {0}".format(l[j])

                        j += 1
        return ('{0}\n{1}\n{2}\n{3}\n{4}').format(ans1, ans2, ans3, ans4, ans5)

import json
import time, sys, datetime
import requests
import http.client, urllib

def bill():
	url = 'https://api.thingspeak.com/channels/455279/fields/6/last.json?api_key=ZDDJL90IXYJOIQ3S&result=1'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response)
	time = data['field6']
    #[(กำลังไฟฟ้า (วัตต์)ชนิดนั้นๆ  x จำนวนเครื่องใช้ไฟฟ้า) ÷1000] x จำนวนชั่วโมงที่ใช้งานใน 1 วัน ÷ 3600 = จำนวนหน่วยหรือยูนิต
    #กำหนดให้ไฟ 50 วัตต์ จำนวน 1 หลอด ยูนิตละ 7 บาท.
    #ค่าไฟต่อวัน = จำนวนยูนิต x 7
    #ค่าไฟต่อเดือน = จำนวนยูนิต x7x30
	time = int(time)
    #print (type(time))
	watt = 50
	amount = 1
	if(time != 0):
		#print ("here")
		total_watt = (watt*amount)/1000
		#print (total_watt)
		unit = (total_watt*time)/3600
		bill_day = unit*7
		bill_month = unit*7*30
		ans_day = "Bill/Day is {0} Bath".format(round(bill_day,2))
		#print (ans_day)
		ans_month = "Bill/Month is {0} Bath".format(round(bill_month,2))
		return('{0}\n{1}').format(ans_day, ans_month)
	elif(time == 0):
		ans_none = "Today you do not have to pay"
		return(ans_none)
            
		
                                
#("LED Bedroom's status is On\n", "LED Stroageroom's status is Off\n", "Fan's status is On\n", "Curtain's status is Off\n", "Springer's status is Off")





                                
