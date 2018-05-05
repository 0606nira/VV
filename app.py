from flask import Flask, request, abort
import time, sys, datetime, os
import json
import send
import weather
import Noty
import detail
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
								label='Garage',
								text='Garage',								
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
				text='LED Bedroom On'
			),
			MessageTemplateAction(
				label='Off',
				text='LED Bedroom Off'
			)
		]
	)
)

# ห้องสัตว์เลี้ยง มีพัดลม จากวัดแสง กับ พัดลม จากวัดอุณหภูมิ
image_carousel_template_message2 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
				action=MessageTemplateAction(
					label='Window',
					text='Window',
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

# หน้าต่าง จากแสง
buttons_template_message21 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
		title='Window',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Window On'
			),
			MessageTemplateAction(
				label='Off',
				text='Window Off'
			),
			MessageTemplateAction(
				label='Sunlight Sensor',
				text='Sunlight Sensor On'
			),
		]
	)
)

# พัดลม จากอุณหภูมิ
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
				label='Temp Sensor',
				text='Temp Sensor On'
			),
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
				text='Garage Light On'
			),
			MessageTemplateAction(
				label='Off',
				text='Garage Light Off'
			),
			MessageTemplateAction(
				label='PIR Sensor',
				text='PIR Sensor On'
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
				label='Humi Sensor',
				text='Humi Sensor On'
			),
		]
	)
)

#Check Home
buttons_template_message5 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://res.cloudinary.com/teepublic/image/private/s--bAhU43hA--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1508124002/production/designs/1975176_1.jpg',
		text='What do you want to check?',
		actions=[
			MessageTemplateAction(
				label='Check Temp',
				text='Check Temp'
			),
			MessageTemplateAction(
				label='Check Humidity',
				text='Check Humidity'
			),
			MessageTemplateAction(
				label='Check Lux',
				text='Check Lux'
			),
			MessageTemplateAction(
				label='Monitor',
				text='Monitor'
			)
		]
	)
)

#Set Up
image_carousel_template_message3 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://orig00.deviantart.net/06f8/f/2012/052/9/e/yuuko_ichihara__s_magic_circle_by_earthstar01-d4qj5jv.png',
				action=MessageTemplateAction(
					label='Check Home',
					text='Check Home',
					)
			),
			ImageCarouselColumn(
				image_url='https://orig00.deviantart.net/06f8/f/2012/052/9/e/yuuko_ichihara__s_magic_circle_by_earthstar01-d4qj5jv.png',
				action=MessageTemplateAction(
					label='Check Electricity Bill',
					text='Check Bill',
					)
			),
			ImageCarouselColumn(
				image_url='https://www.eg.mahidol.ac.th/egmu/images/egmu.jpg',
				action=MessageTemplateAction(
					label='Mahidol',
					text='Mahidol',								
				)
			),
		]
	)
)

#อากาศ
buttons_template_message6 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Weather_Rounded.svg/1024px-Weather_Rounded.svg.png',
		text='Which station you would like to?',
		actions=[
			MessageTemplateAction(
				label='Bangkok',
				text='BANGKOK'
			),
			MessageTemplateAction(
				label='Nakhonpathom',
				text='NAKHONPATHOM'
			),
			MessageTemplateAction(
				label='Chiang Mai',
				text='CHIANG MAI'
			),
			MessageTemplateAction(
				label='Phuket',
				text='PHUKET'
			),
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
	#global multicasts ไม่ต้องใส่
	if(message == 'Home'): #แสดงเมนูห้องทั้งหมด 4 ห้อง
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message1)	
	elif(message == 'Bed Room'): #แสดงเมนูของห้องนอน
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message1)
	elif(message == 'LED Bedroom On'):
		send.send_values1(1) #ส่งคำสั่งไปอัพเดทข้อมูลในเว็บ Thingspeak ให้เป็น 1 คือเปิด
		if(Noty.notification1() == '1'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='LED Bedroom On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="LED Bedroom didn't on"))
	elif(message == 'LED Bedroom Off'):
		send.send_values1(0) #ส่งคำสั่งไปอัพเดทข้อมูลในเว็บ Thingspeak ให้เป็น 0 คือเปิด
		if (Noty.notification1() == '0'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='LED Bedroom Off at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="LED Bedroom didn't off"))
	elif(message == 'Living Room'): #แสดงเมนูห้องนั่งเล่น มี 2 อุปกรณ์ คือม่านกับพัดลม
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message2)
	elif(message == 'Window'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message21)
	elif(message == 'Window On'):
		send.send_values4(1)
		if(Noty.notification4() == '1'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Window On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Window didn't on"))
		detail.detail_lux()	
	elif(message == 'Window Off'):
		send.send_values4(0)
		if(Noty.notification4() == '0'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Window Off at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="window didn't off"))
		detail.detail_lux()	
	elif(message == 'Sunlight Sensor On'):
		send.send_values4(2)
		if(Noty.notification4() == '2'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Sunlight Sensor On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Sunlight Sensor didn't on"))
	elif(message == 'Fan'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message22)
	elif(message == 'Fan On'):
		send.send_values3(1)
		if(Noty.notification3() == '1'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Fan On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Fan didn't on"))
		detail.detail_temp()
	elif(message == 'Fan Off'):
		send.send_values3(0)
		if(Noty.notification3() == '0'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Fan Off at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Fan didn't off"))
		detail.detail_temp()
	elif(message == 'Temp Sensor On'):
		send.send_values3(2)
		if(Noty.notification3() == '2'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Temp Sensor On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Temp Sensor didn't on"))
	elif(message == 'Garage'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message3)
	elif(message == 'Garage Light On'):
		send.send_values2(1)
		if(Noty.notification2() == '1'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='LED Garage On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="LED Garage can't on"))
	elif(message == 'Garage Light Off'):
		send.send_values2(0)
		if(Noty.notification2() == '0'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='LED Garage Off at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="LED Garage didn't off"))
	elif(message == 'PIR Sensor On'):
		send.send_values2(2)
		if(Noty.notification2() == '2'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='PIR Sensor On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="PIR Sensor didn't on"))
	elif(message == 'Landscape'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message4)
	elif(message == 'Springer On'):
		send.send_values5(1)
		if(Noty.notification5() == '1'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Springer On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Springer didn't on"))
		detail.detail_humi()
	elif(message == 'Springer Off'):
		send.send_values5(0)	
		if(Noty.notification5() == '0'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Springer Off at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Springer didn't off"))
		detail.detail_humi()
	elif(message == 'Humi Sensor On'):
		send.send_values5(2)	
		if(Noty.notification5() == '2'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Humi Sensor on at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Humi Sensor didn't on"))
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
	elif(message == 'Check Temp'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="Temp. is '{0}' check at '{1}'".format(detail.detail_temp(), timeat)))
	elif(message == 'Check Humidity'):
		#detail.detail_humi()
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="Humidity. is '{0}' check at '{1}'".format(detail.detail_humi(), timeat)))
	elif(message == 'Check Lux'):
		#detail.detail_lux()
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="LUX. is '{0}' check at '{1}'".format(detail.detail_lux(), timeat)))
	elif(message == 'Monitor'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="{}".format(Noty.monitor())))
	elif(message == 'Check Home'):
		line_bot_api.reply_message(
			event.reply_token, 
			buttons_template_message5)
	elif(message == 'Weather'):
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message6)
	elif(message == 'BANGKOK'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="{}".format(weather.weather('BANGKOK METROPOLIS'))))
	elif(message == 'NAKHONPATHOM'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="{}".format(weather.weather('NAKHONPATHOM'))))
	elif(message == 'CHIANG MAI'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="{}".format(weather.weather('CHIANG MAI'))))
	elif(message == 'PHUKET'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="{}".format(weather.weather('PHUKET'))))
	elif(message == 'Set Up'): #เมื่อต้องการตั้งค่า
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message3)
	elif(message == 'Mahidol'):
		line_bot_api.reply_message(
			event.reply_token,
			LocationMessage(
				title='Faculty of Engineering, Mahidol University', address='Salaya, Phutthamonthon District, Nakhon Pathom 73170',
				latitude=13.796024, longitude=100.325066
			)
		)
	elif(message == 'Check Bill'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="{}".format(Noty.bill())))

		
#@handler.add(MessageEvent, message=LocationMessage)
#def handle_location_message(event):
	#message = event.message.text
	#if(message == 'Location'):
		#line_bot_api.reply_message(
			#event.reply_token,
			#LocationMessage(
				#title=event.message.title, address=event.message.address,
				#latitude=event.message.latitude, longitude=event.message.longitude
			#)
		#)
	#elif(message == 'Mahidol'):
		#line_bot_api.reply_message(
			#event.reply_token,
			#LocationMessage(
				#title='Faculty of Engineering, Mahidol University', address='Salaya, Phutthamonthon District, Nakhon Pathom 73170',
				#latitude=13.796024, longitude=100.325066
			#)
		#)				


#@handler.add(MessageEvent, message=LocationMessage)
#def handle_location_message(event):
	#message = event.message.text
	#if(message == 'Location'):
	#line_bot_api.reply_message(
		#	event.reply_token,
			#LocationMessage(
			#	title='Faculty of Engineering, Mahidol University', address='Salaya, Phutthamonthon District, Nakhon Pathom 73170',
			#	latitude=13.796024, longitude=100.325066
			#)
		#)				


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