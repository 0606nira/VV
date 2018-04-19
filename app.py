from flask import Flask, request, abort
import time, sys, datetime, os
import asyncio
import json
import send
import mode
import requests 
import http.client, urllib
from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
 SourceUser, SourceGroup, SourceRoom,
 TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
 ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
 CarouselTemplate, CarouselColumn, PostbackEvent, ImageCarouselTemplate,
 StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
 ImageMessage, VideoMessage, AudioMessage, ImageCarouselColumn,
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent, DatetimePickerTemplateAction,
 )


app = Flask(__name__)

line_bot_api = LineBotApi('MEMIUEV7R2dzmxXVTkQRcgply61mFF16A/BEXFbh01XuuN1oGwhLH5t+GbxcJRIXEsiioQe7xhs0mluGITwfR55jRSRsd3R+JTBz6Z1O3Q+Ei0OIYS2QT0Mg86n6UZowtp0nO7HWmJBQJoCc4nSyMgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('13c1dcf5fa5fe8495b15f1ab271791f5')

timeis = time.localtime()
timeat = time.strftime('%A %d %B %Y, %H:%M:%S', timeis) # กำหนดรูปแบบเวลา
now = datetime.datetime.now()

multicasts = []
timesetup = {}

dummy = 0

image_carousel_template_message1 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://i1.wp.com/www.kmusic2blog.com/wp-content/uploads/2017/02/cover.jpg',
				action=MessageTemplateAction(
					label='Bed Room',
					text='Bed Room',
							)
					),
					ImageCarouselColumn(
						image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
						action=MessageTemplateAction(
								label='Living Room',
								text='Living Room',								
							)
					),
				ImageCarouselColumn(
						image_url='https://img00.deviantart.net/09f6/i/2016/141/d/0/bts___the_most_beautiful_moment_in_life__yf_by_5secondsofdemi-da3a3br.jpg',
						action=MessageTemplateAction(
								label='Storage Room',
								text='Storage Room',								
							)
					),
				ImageCarouselColumn(
						image_url='https://i0.wp.com/www.kmusic2blog.com/wp-content/uploads/2016/10/cover-1024x1024.jpg',
						action=MessageTemplateAction(
								label='Landscape',
								text='Landscape',								
							)
					)
			]
		)
)

# ห้องนอนมีไฟ 
buttons_template_message1 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://i1.wp.com/www.kmusic2blog.com/wp-content/uploads/2017/02/cover.jpg',
		title='Light',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Bedroom Light On'
			),
			MessageTemplateAction(
				label='Off',
				text='Bedroom Light Off'
			)
		]
	)
)

# ห้องสัตว์เลี้ยง มีม่าน จากวัดแสง กับ พัดลม จากวัดอุณหภูมิ
image_carousel_template_message2 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
				action=MessageTemplateAction(
					label='Curtain',
					text='Curtain',
							)
					),
			ImageCarouselColumn(
				image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
				action=MessageTemplateAction(
					label='Fan',
					text='Fan',								
				)
			),
		]
	)
)

# ผ้าม่าน
buttons_template_message21 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
		title='Curtain',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Curtain On'
			),
			MessageTemplateAction(
				label='Off',
				text='Curtain Off'
			)
		]
	)
)

# พัดลม *******
buttons_template_message22 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
		title='Fan',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Fan On'
			),
			MessageTemplateAction(
				label='Off',
				text='Fan Off'
			),
			MessageTemplateAction(
				label='Check Temp',
				text='Check Temp'
			)
		]
	)
)

# ไฟห้องเก็บของ จากวัดเคลื่อนไหว
buttons_template_message3 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://img00.deviantart.net/09f6/i/2016/141/d/0/bts___the_most_beautiful_moment_in_life__yf_by_5secondsofdemi-da3a3br.jpg',
		title='Light',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Storageroom Light On'
			),
			MessageTemplateAction(
				label='Off',
				text='Storageroom Light Off'
			)
		]
	)
)

# สปริงเกอร์สนามหญ้า จากความชื้นดิน *****
buttons_template_message4 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://i0.wp.com/www.kmusic2blog.com/wp-content/uploads/2016/10/cover-1024x1024.jpg',
		title='Springer',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Springer On'
			),
			MessageTemplateAction(
				label='Off',
				text='Springer Off'
			),
			MessageTemplateAction(
				label='Check Humidity',
				text='Check Humidity'
			)
		]
	)
)

#ตั้งค่า
buttons_template_message5 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://res.cloudinary.com/teepublic/image/private/s--bAhU43hA--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1508124002/production/designs/1975176_1.jpg',
		text='What do you want to set up?',
		actions=[
			MessageTemplateAction(
				label='MODE',
				text='Set up MODE'
			),
			PostbackTemplateAction(
				label='Notification',
				data='noti_postback',
				text='Set up notification'
			),
			MessageTemplateAction(
				label='Nothing',
				text='Cancel set up'
			)
		]
	)
)

#ตั้งค่าแจ้งเตือน 
buttons_template_message6 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://res.cloudinary.com/teepublic/image/private/s--BRE04nGW--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1508124241/production/designs/1975184_1.jpg',
		text='Please select',
		actions=[
			PostbackTemplateAction(
				label='Add Notify',
				data='add_noti',
				text='Add success'
			),
			PostbackTemplateAction(
				label='Remove Notify',
				data='remove_noti',
				text='Remove success'
			),
			MessageTemplateAction(
				label='Check list', #ไว้เช็ค ID ต่างๆที่เก็บไว้ใน list multicasts
				text='Check list'
			),
			MessageTemplateAction(
				label='Nothing',
				text='Cancel set up'
			)
		]
	)
)

#ตั้งค่า MODE
buttons_template_message7 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://res.cloudinary.com/teepublic/image/private/s--BRE04nGW--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1508124241/production/designs/1975184_1.jpg',
		text='Please select',
		actions=[
			MessageTemplateAction(
				label='Turn On Automation',
				text='Turn On Automation'
			),
			MessageTemplateAction(
				label='Turn Off Automation',
				text='Turn Off Automation'
			)
		]
	)
)

@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature'] 

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	
	# handle webhook body
	try:
		handler.handle(body, signature)
	except LineBotApiError as e:
		print(e.status_code)
		print(e.error.message)
		print(e.error.details)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
	message = event.message.text
	global multicasts
	if(message == 'Home'): #แสดงเมนูห้องทั้งหมด 4 ห้อง
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message1)	
	elif(message == 'Bed Room'): #แสดงเมนูของห้องนอน
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message1)
	elif(message == 'Bedroom Light On'):
		send.send_values(1) #ส่งคำสั่งไปอัพเดทข้อมูลในเว็บ Thingspeak ให้เป็น 1 คือเปิด
		notification()
	elif(message == 'Bedroom Light Off'):
		send.send_values(0) #ส่งคำสั่งไปอัพเดทข้อมูลในเว็บ Thingspeak ให้เป็น 0 คือเปิด
		notification()
	elif(message == 'Living Room'): #แสดงเมนูห้องนั่งเล่น มี 2 อุปกรณ์ คือม่านกับพัดลม
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message2)
	elif(message == 'Curtain'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message21)
	elif(message == 'Curtain On'):
		send.send_values(7)
		notification()
	elif(message == 'Curtain Off'):
		send.send_values(6)
		notification()
	elif(message == 'Fan'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message22)
	elif(message == 'Fan On'):
		send.send_values(5)
		notification()
		detail_temp()
	elif(message == 'Fan Off'):
		send.send_values(4)
		notification()
		detail_temp()
	elif(message == 'Storage Room'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message3)
	elif(message == 'Storageroom Light On'):
		send.send_values(3)
		notification()
	elif(message == 'Storageroom Light Off'):
		send.send_values(2)
		notification()		
	elif(message == 'Landscape'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message4)
	elif(message == 'Springer On'):
		send.send_values(9)
		notification()
	elif(message == 'Springer Off'):
		send.send_values(8)	
		notification()		
	elif(message == 'Bye'): #เตะ bot ออกจากกลุุ่มหรือห้องแชท
		if isinstance(event.source, SourceGroup):
			line_bot_api.reply_message(
				event.reply_token, TextMessage(text='Leaving group'))
			line_bot_api.leave_group(event.source.group_id)
		elif isinstance(event.source, SourceRoom):
			line_bot_api.reply_message(
				event.reply_token, TextMessage(text='Leaving room'))
			line_bot_api.leave_room(event.source.room_id)
		else:
			line_bot_api.reply_message(
				event.reply_token,
				TextMessage(text="Can't Leave"))
	elif(message == 'Set Up'): #เมื่อต้องการตั้งค่า
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message5)
	elif(message == 'Set up MODE'):
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message7)
	elif(message == 'Turn Off Automation'):
		line_bot_api.reply_message(
			event.reply_token, TextMessage(text='Turn Off Automation'))
		mode.mode(0)
	elif(message == 'Turn On Automation'):
		line_bot_api.reply_message(
			event.reply_token, TextMessage(text='Turn On Automation'))
		mode.mode(1)
	elif(message == 'Check list'):
		line_bot_api.reply_message(
			event.reply_token, TextMessage(text='%s' %multicasts))
	elif(message == 'Check Temp'):
		detail_temp()
	elif(message == 'Check Temp'):
		detail_humi()
		
@handler.add(PostbackEvent)
def handle_postback(event):
	postback = event.postback.data
	global multicasts
	if(postback == 'noti_postback'): #ตัวเลือกว่าต้องการตั้งค่าเกี่ยวกับการแจ้งเตือน
		line_bot_api.reply_message(
			event.reply_token, 
			buttons_template_message6)		
	elif(postback == 'add_noti'): #เมื่อต้องการรับค่าแจ้งเตือน
		if isinstance(event.source, SourceUser): #ถ้าเป็นห้องแชทแบบ 1 ต่อ 1
			if(event.source.user_id in multicasts): #ถ้ามี ID นั้นใน list อยู่แล้ว
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='you already on notify'))
			else:
				multicasts.append(event.source.user_id)#เพิ่ม ID ลงใน list
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='your id is %s add' %event.source.user_id))
				print (multicasts)
		elif isinstance(event.source, SourceGroup):
			if(event.source.group_id in multicasts):
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='you already on notify'))
			else:
				multicasts.append(event.source.group_id)
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='your group id is %s add' %event.source.group_id))					
		elif isinstance(event.source, SourceRoom):
			if(event.source.room_id in multicasts):
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='you already on notify'))
			else:
				multicasts.append(event.source.room_id)
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='your room id is %s add' %event.source.room_id))
				print (multicasts)
	elif(postback == 'remove_noti'): #ถ้าไม่ต้องการรับการแจ้งเตือนแล้ว
		if isinstance(event.source, SourceUser):
			if(event.source.user_id in multicasts): #ถ้ามี ID นั้นใน list อยู่แล้ว
				multicasts.remove(event.source.user_id)#ลบ ID นั้นออกจาก list
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='your id is %s re' %event.source.user_id))
			else:
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text="your notify didn't set"))
		elif isinstance(event.source, SourceGroup):
			if(event.source.group_id in multicasts):
				multicasts.remove(event.source.group_id)
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='your group id is %s re' %event.source.group_id))
			else:
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text="your notify didn't set"))
		elif isinstance(event.source, SourceRoom):
			if(event.source.room_id in multicasts):
				multicasts.remove(event.source.room_id)
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text='your room id is %s re' %event.source.room_id))
			else:
				line_bot_api.reply_message(
					event.reply_token, 
					TextSendMessage(text="your notify didn't set"))
					
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
	message = event.message.text
	if(message == 'Location'):
		line_bot_api.reply_message(
			event.reply_token,
			LocationMessage(
				title='Faculty of Engineering, Mahidol University', address='Salaya, Phutthamonthon District, Nakhon Pathom 73170',
				latitude=13.796024, longitude=100.325066
			)
		)

def notification():
	global multicasts
	global dummy #ตั้งเป็นตัวแปรหลอก
	print ('dummy: ', dummy)
	#last_detect = datetime.datetime.now()
	#url GET อ่านข้อมูล
	url = 'https://api.thingspeak.com/channels/455279/feeds.json?api_key=ZDDJL90IXYJOIQ3S&results=2'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['feeds'][1]['entry_id']
	print ('entry_status: ', entry_status)
	last_status = data['feeds'][1]['field1'] #อ่านสถานะของอุปกรณ์
	if(entry_status != dummy): #ถ้าไม่เท่ากันแสดงว่ามีการเปลี่ยนแปลงค่าใน channel
		if(last_status != None):
			dummy = entry_status #ให้dummy เท่ากับentry_status(คือจำนวนที่มีการเปลี่ยนแปลงใน channelนั้นๆ)
			print ('dummy1: ', dummy)
				if(last_status == '0'):
					for i in range(0, len(multicasts)):
						line_bot_api.push_message(
							multicasts[i], 
							TextSendMessage(text='Light Bedroom Off at ' +timeat))
				elif(last_status == '1'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Light Bedroom On at ' +timeat))
				elif(last_status == '2'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Light Stroageroom Off at ' +timeat))
				elif(last_status == '3'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Light Stroageroom On at ' +timeat))
				elif(last_status == '4'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text="Fan Off at '{0}'".format(timeat)))
				elif(last_status == '5'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Fan On at ' +timeat))
				elif(last_status == '6'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Curtain Off at ' +timeat))
				elif(last_status == '7'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Curtain On at ' +timeat))
				elif(last_status == '8'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Springer Off at ' +timeat))
				elif(last_status == '9'):
					line_bot_api.push_message(
						multicasts[i], 
						TextSendMessage(text='Springer On at ' +timeat))
						
def detail_temp():
	url = 'https://api.thingspeak.com/channels/455279/fields/2/last.json?api_key=ZDDJL90IXYJOIQ3S'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['entry_id']
	print ('entry_status: ', entry_status)
	last_temp = data['field2']
	#last_humi = data['feeds'][0]['field3']
	#last_pir = data['feeds'][0]['field4']
	#last_lux = data['feeds'][0]['field5']
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text='Temp. is ' +last_temp))

def detail_humi():
	url = 'https://api.thingspeak.com/channels/455279/fields/2/last.json?api_key=ZDDJL90IXYJOIQ3S'
	response = urllib.request.urlopen(url) #ส่งคำขอขอข้อมูล
	data = json.load(response) #แปลงข้อมูล json ที่ได้รับมา
	entry_status = data['entry_id']
	print ('entry_status: ', entry_status)
	#last_temp = data['field2']
	last_humi = data['field3']
	#last_pir = data['feeds'][0]['field4']
	#last_lux = data['feeds'][0]['field5']
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text='Humidity is ' +last_humi))

	#@handler.add(MessageEvent, message=LocationMessage)
#def handle_location_message(event):
    #line_bot_api.reply_message(
       # event.reply_token,
       # LocationSendMessage(
            #title=event.message.title, address=event.message.address,
           # latitude=event.message.latitude, longitude=event.message.longitude
        #)
   # )
#@handler.add(MessageEvent, message=StickerMessage)
#def handle_sticker_message(event):
	#line_bot_api.reply_message(
		#event.reply_token,
		#StickerSendMessage(
		#	package_id=event.message.package_id,
		#	sticker_id=event.message.sticker_id
	# )
	
if __name__ == "__main__":
	app.run(debug=True)