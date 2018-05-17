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
timeat = time.strftime('%A %d %B %Y', timeis) # กำหนดรูปแบบเวลา
now = datetime.datetime.now()


image_carousel_template_message1 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://i.pinimg.com/originals/e0/b4/6f/e0b46f97680a9fa9a72028b3844555aa.jpg',
				action=MessageTemplateAction(
					label='Bed Room',
					text='Bed Room',
					)
				),
			ImageCarouselColumn(
				image_url='https://st.hzcdn.com/simgs/bbc1af3d04086530_4-3375/contemporary-family-room.jpg',
				action=MessageTemplateAction(				
					label='Living Room',
					text='Living Room',
					)					
				),
			ImageCarouselColumn(
				image_url='https://2p2bboli8d61fqhjiqzb8p1a-wpengine.netdna-ssl.com/wp-content/uploads/2016/04/iron-man-2-audi-r8-680x481.jpg', 
				action=MessageTemplateAction(
					label='Garage',
					text='Garage',	
					)					
				),
			ImageCarouselColumn(
				image_url='https://avatars.mds.yandex.net/get-pdb/251121/85e9f348-b5ff-41ae-8ad8-0db1a8db8293/s800', 
				action=MessageTemplateAction(
					label='Garden',
					text='Garden',								
					)
				)
			]
		)
)

# ห้องนอนมีไฟ 
buttons_template_message1 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://techannouncer.com/wp-content/uploads/2017/09/Darkroom-lamp-Market-1.jpg',
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

# ห้องนั่งเล่น มีพัดลม จากวัดแสง กับ พัดลม จากวัดอุณหภูมิ
image_carousel_template_message2 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://www.reggie.net/photos/england/cambridgeshire/cambridge/downing_college/east_range/10021415_bicycle_window_boxes_sandstone_downing_college_cambridge-600.jpg',
				action=MessageTemplateAction(
					label='Window',
					text='Window',
							)
					),
			ImageCarouselColumn(
				image_url='https://ceilingfancomparison.com/wp-content/uploads/2017/01/Buying-a-Ceiling-Fan-with-Lights.jpg',
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
		thumbnail_image_url='https://www.reggie.net/photos/england/cambridgeshire/cambridge/downing_college/east_range/10021415_bicycle_window_boxes_sandstone_downing_college_cambridge-600.jpg',
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
		thumbnail_image_url='https://ceilingfancomparison.com/wp-content/uploads/2017/01/Buying-a-Ceiling-Fan-with-Lights.jpg',
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
				label='DHT11 Sensor',
				text='DHT11 Sensor On'
			),
		]
	)
)

# ไฟห้องเก็บของ จากวัดเคลื่อนไหว
buttons_template_message3 = TemplateSendMessage(
	alt_text='Buttons template',
	template=ButtonsTemplate(
		thumbnail_image_url='https://images.pexels.com/photos/185699/pexels-photo-185699.jpeg?auto=compress&cs=tinysrgb&h=350',
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
		thumbnail_image_url='https://images.pexels.com/photos/212324/pexels-photo-212324.jpeg?auto=compress&cs=tinysrgb&h=350',
		title='Sprinkler',
		text='Please select',
		actions=[            
			MessageTemplateAction(
				label='On',
				text='Sprinkler On'
			),
			MessageTemplateAction(
				label='Off',
				text='Sprinkler Off'
			),
			MessageTemplateAction(
				label='Moisture Sensor',
				text='Moisture Sensor On'
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
				image_url='https://res.cloudinary.com/teepublic/image/private/s--bAhU43hA--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1508124002/production/designs/1975176_1.jpg',
				action=MessageTemplateAction(
					label='Check Home',
					text='Check Home',
					)
			),
			ImageCarouselColumn(
				image_url='https://orig00.deviantart.net/06f8/f/2012/052/9/e/yuuko_ichihara__s_magic_circle_by_earthstar01-d4qj5jv.png',
				action=MessageTemplateAction(
					label='Check E-Bill',
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
#Humidity
image_carousel_template_message4 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://i.pinimg.com/736x/d3/2b/6f/d32b6f83b1b8fedb83af385b5eeb8e9f--magic-symbols-card-captor.jpg',
				action=MessageTemplateAction(
					label='HumidityAir',
					text='Check Humidity in the Air',
					)
			),
			ImageCarouselColumn(
				image_url='https://i.pinimg.com/736x/d3/2b/6f/d32b6f83b1b8fedb83af385b5eeb8e9f--magic-symbols-card-captor.jpg',
				action=MessageTemplateAction(
					label='HumiditySoil',
					text='Check Humidity in the Soil',
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
		detail.detail_humi_air()
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
	elif(message == 'DHT11 Sensor On'):
		send.send_values3(2)
		if(Noty.notification3() == '2'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='DHT11 Sensor On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="DHT11 Sensor didn't on"))
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
	elif(message == 'Garden'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message4)
	elif(message == 'Sprinkler On'):
		send.send_values5(1)
		if(Noty.notification5() == '1'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Sprinkler On at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Sprinkler didn't on"))
		detail.detail_humi_soil()
	elif(message == 'Sprinkler Off'):
		send.send_values5(0)	
		if(Noty.notification5() == '0'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Sprinkler Off at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Sprinkler didn't off"))
		detail.detail_humi_soil()
	elif(message == 'Moisture Sensor On'):
		send.send_values5(2)	
		if(Noty.notification5() == '2'):
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text='Moisture Sensor on at ' +timeat))
		else:
			line_bot_api.reply_message(
				event.reply_token, 
				TextSendMessage(text="Moisture Sensor didn't on"))
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
			image_carousel_template_message4)
	elif(message == 'Check Humidity in the Soil'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="Humidity Soil is '{0}' check at '{1}'".format(detail.detail_humi_soil(), timeat)))
	elif(message == 'Check Humidity in the Air'):
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text="Humidity Air is '{0}' check at '{1}'".format(detail.detail_humi_air(), timeat)))
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
			TextSendMessage(text="{0}\n{1}".format(timeat, Noty.bill())))
	else:
		line_bot_api.reply_message(
			event.reply_token, 
			StickerSendMessage(
				package_id='2',
				sticker_id='149'
				))
				
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )	

@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="""\
Hello I'm Sweet Home IEMU ☆*:.｡.o(≧▽≦)o.｡.:*☆
	Thank for invited me.
	｡☆✼★━━━━━━━━━━━━★✼☆｡
*+:｡.｡For Group/Room chat｡.｡:+*
Please send the following text with the same alphabet.
"Home" : use for control your house.
"Set Up" : use for check any data and information.
"Weather" : use for check a temperature from TMD.
"Bye" : use for delete me from this chat.
		"""))
		
@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="""\
Hello to Sweet Home IEMU ☆*:.｡.o(≧▽≦)o.｡.:*☆
	Thank for added me.
	｡☆✼★━━━━━━━━━━━━★✼☆｡
You don't need to interact with me by a text.
Just try to use Rich Menu from below.
		"""))
		


if __name__ == "__main__":
	app.run(debug=True)

	
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
	
