﻿from flask import Flask, request, abort
import time, sys, datetime
import json
import asyncio
import send
import noti
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
multicasts = []

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

# ห้องนอนมีไฟ ตั้งเวลาแจ้งเตือนตอน 9 โมง
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

# พัดลม
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
            URITemplateAction(
                label='Check Temp',
                uri='https://www.youtube.com/watch?v=kTlv5_Bs8aw'
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

# สปริงเกอร์สนามหญ้า จากความชื้นดิน
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
            URITemplateAction(
                label='Check Humidity',
                uri='https://www.youtube.com/watch?v=7OX7dIRReSA&list=PL_Cqw69_m_yzbMVGvQA8QWrL_HdVXJQX7&index=15'
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
			DatetimePickerTemplateAction(
				label='Time',
				data='time_postback',
				mode='time'
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
				text='%s' %multicasts
			),
			MessageTemplateAction(
				label='Nothing',
				text='Cancel set up'
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
	except linebot.exceptions.LineBotApiError as e:
		print(e.status_code)
		print(e.error.message)
		print(e.error.details)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
	message = event.message.text

	if(message == 'Home'): #แสดงเมนูห้องทั้งหมด 4 ห้อง
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message1)	
	elif(message == 'Bed Room'): #แสดงเมนูของห้องนอน
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message1)
	elif(message == 'Bedroom Light On'):
		send.send_values1(1) #ส่งคำสั่งไปอัพเดทข้อมูลในเว็บ Thingspeak ให้เป็น 1 คือเปิด
	elif(message == 'Bedroom Light Off'):
		send.send_values1(0) #ส่งคำสั่งไปอัพเดทข้อมูลในเว็บ Thingspeak ให้เป็น 0 คือเปิด
	elif(message == 'Living Room'): #แสดงเมนูห้องนั่งเล่น มี 2 อุปกรณ์ คือม่านกับพัดลม
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message2)
	elif(message == 'Curtain'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message21)
	elif(message == 'Curtain On'):
		send.send_values4(1)
	elif(message == 'Curtain Off'):
		send.send_values4(0)
	elif(message == 'Fan'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message22)
	elif(message == 'Fan On'):
		send.send_values3(1)
	elif(message == 'Fan Off'):
		send.send_values3(0)
	elif(message == 'Storage Room'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message3)
	elif(message == 'Storageroom Light On'):
		send.send_values2(1)
	elif(message == 'Storageroom Light Off'):
		send.send_values2(0)		
	elif(message == 'Landscape'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message4)
	elif(message == 'Springer On'):
		send.send_values5(1)
	elif(message == 'Springer Off'):
		send.send_values5(0)			
	elif(message == 'Locatione'): #แสดงตำแหน่งมหิดล แต่ยังไม่ขึ้นอะไรเลย
		line_bot_api.reply_message(
			event.reply_token, 
			LocationSendMessage(
				title='my location', 
				address='Mahidol University', 
				latitude=13.794578, 
				longitude=100.323417))
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
			
@handler.add(PostbackEvent)
def handle_postback(event):
	postback = event.postback.data
	if(postback == 'time_postback'): #รับค่าเวลาที่เลือกได้มา ยังไม่ได้กำหนดว่าจะเอาไปทำอะไร
		line_bot_api.reply_message(
			event.reply_token, 
			TextSendMessage(text='Time to wake up is %s' %event.postback.params['time']))
		print (event.postback.params['time'])
	elif(postback == 'noti_postback'): #ตัวเลือกว่าต้องการตั้งค่าเกี่ยวกับการแจ้งเตือน
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

def n():
while True:
	if (noti.notification() == ('0', 1)):
		print ('Light Off ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Light Bedroom Off when ' +timeat))
	elif (noti.notification() == ('1', 1)):
		print ('Light On ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Light Bedroom On when ' +timeat))
	elif (noti.notification() == ('0', 2)):
		print ('Light Off ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Light Stroageroom Off when ' +timeat))
	elif (noti.notification() == ('1', 2)):
		print ('Light On ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Light Stroageroom On when ' +timeat))
	elif (noti.notification() == ('0', 3)):
		print ('Fan Off ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Fan Off when ' +timeat))
	elif (noti.notification() == ('1', 3)):
		print ('Fan On ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Fan On when ' +timeat))
	elif (noti.notification() == ('0', 4)):
		print ('Curtain Off ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Curtain Off when ' +timeat))
	elif (noti.notification() == ('1', 4)):
		print ('Curtain On ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Curtain On when ' +timeat))
	elif (noti.notification() == ('0', 5)):
		print ('Springer Off ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Springer Off when ' +timeat))
	elif (noti.notification() == ('1', 5)):
		print ('Springer On ' +timeat)
		line_bot_api.push_message(
			'U5db26ce3aad1c4d83691ea5d6992116a', 
			TextSendMessage(text='Springer On when ' +timeat))

	time.sleep(5)
	
if __name__ == "__main__":
    app.run(debug=True)