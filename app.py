from flask import Flask, request, abort
import time, sys
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
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
 )

app = Flask(__name__)

line_bot_api = LineBotApi('MEMIUEV7R2dzmxXVTkQRcgply61mFF16A/BEXFbh01XuuN1oGwhLH5t+GbxcJRIXEsiioQe7xhs0mluGITwfR55jRSRsd3R+JTBz6Z1O3Q+Ei0OIYS2QT0Mg86n6UZowtp0nO7HWmJBQJoCc4nSyMgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('13c1dcf5fa5fe8495b15f1ab271791f5')

API_KEY_WRITE = 'WWRZDTPBUN0O18FM'

def send_values(light):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field1': light,
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        print ('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            print ('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
        print ("connection failed", sys.exc_info())

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
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	message = event.message.text

	if(message == 'Go to HOME'):
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message1)
	elif(message == 'Bed Room'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message1)
	elif(message == 'Pet Room'): 
		line_bot_api.reply_message(
			event.reply_token,
			image_carousel_template_message2)
	elif(message == 'Storage Room'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message3)
	elif(message == 'Landscape'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message4)
	elif(message == 'Curtain'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message21)
	elif(message == 'Fan'): 
		line_bot_api.reply_message(
			event.reply_token,
			buttons_template_message22)
	elif(message == 'Bedroom Light On'):
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Light On"))
		send_values(1)
	elif(message == 'Bedroom Light Off'):
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Light On"))
		send_values(0)
	else:
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Have a good day"))

image_carousel_template_message1 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='http://zlregata.com/wp-content/uploads/2017/12/Fresh-Images-of-Go-dark-in-style-inside-the-bedroom.jpg-Blue-Gray-Bedroom-Paint-Collection-Decor.jpg',
				action=MessageTemplateAction(
					label='Bed Room',
					text='Bed Room',
							)
					),
					ImageCarouselColumn(
						image_url='https://www.ceramicarondine.it/media//catalogimages/MS6/HD_AMB_1.jpg',
						action=MessageTemplateAction(
								label='Pet Room',
								text='Pet Room',								
							)
					),
				ImageCarouselColumn(
						image_url='http://www.ebootcamp.org/l/2018/02/living-room-cabinet-design-ideas-clothing-storage-ideas-for-small-bedrooms-wall-storage-cabinets-for-bedrooms-cabinets-for-sale.jpg',
						action=MessageTemplateAction(
								label='Storage Room',
								text='Storage Room',								
							)
					),
				ImageCarouselColumn(
						image_url='http://www.catsandflorals.com/wp-content/uploads/2017/11/cool-tips-for-front-yard-landscaping-ideas-front-house-garden-design-together-with-stunning-garden-design-ideas-for-front-of-house-1024x768.jpg',
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
        thumbnail_image_url='https://hamipara.com/wp-content/uploads/2017/06/Bedroom-Overhead-Light-Fixtures-Gallery-With-Vintage-Ceiling-Pictures-Antique-1024x768.jpg',
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
				image_url='https://cdn.shopify.com/s/files/1/1992/6569/products/red-velvet-curtains_530x@2x.jpg?v=1502874704',
				action=MessageTemplateAction(
					label='Curtain',
					text='Curtain',
							)
					),
					ImageCarouselColumn(
						image_url='http://autocorrect.us/wp-content/uploads/2018/01/ceiling-fan-light-kit-adapter-ceiling-fan-light-kit-replacement-intended-for-measurements-1024-x-768.jpg',
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
        thumbnail_image_url='https://cdn.shopify.com/s/files/1/1992/6569/products/red-velvet-curtains_530x@2x.jpg?v=1502874704',',
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
        thumbnail_image_url='http://autocorrect.us/wp-content/uploads/2018/01/ceiling-fan-light-kit-adapter-ceiling-fan-light-kit-replacement-intended-for-measurements-1024-x-768.jpg',
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
        thumbnail_image_url='http://theandroidworkshop.com/wp-content/uploads/2018/03/cloud-pendant-light-2013-jonas-wagell-design-architecture-cloud-pendant-lamp-1024x1024.jpg',
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
        thumbnail_image_url='https://imagesvc.timeincapp.com/v3/mm/image?url=https%3A%2F%2Fimg1.southernliving.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fmedium_2x%2Fpublic%2Fimage%2F2016%2F03%2Fmain%2Fgasesp021024861.jpg%3Fitok%3DjJb-NiL8&w=800&q=85',
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


   
if __name__ == "__main__":
    app.run(debug=True)