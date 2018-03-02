from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerMessage, StickerSendMessage, TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction, ImageCarouselTemplate, ImageCarouselColumn, ButtonsTemplate, URITemplateAction, 
)

app = Flask(__name__)

line_bot_api = LineBotApi('MEMIUEV7R2dzmxXVTkQRcgply61mFF16A/BEXFbh01XuuN1oGwhLH5t+GbxcJRIXEsiioQe7xhs0mluGITwfR55jRSRsd3R+JTBz6Z1O3Q+Ei0OIYS2QT0Mg86n6UZowtp0nO7HWmJBQJoCc4nSyMgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('13c1dcf5fa5fe8495b15f1ab271791f5')

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

	if(message == 'Home'):
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
	elif(message == 'Lawn Home'): 
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
	else:
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Have a good day"))


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
								label='Pet Room',
								text='Pet Room',								
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
								label='Lawn Home',
								text='Lawn Home',								
							)
					)
			]
		)
)

# ��ͧ�͹��� �����������͹�͹ 9 ���
buttons_template_message1 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i1.wp.com/www.kmusic2blog.com/wp-content/uploads/2017/02/cover.jpg',
        title='Menu',
        text='Please select',
        actions=[            
            MessageTemplateAction(
                label='On',
                text='Light on'
            ),
            MessageTemplateAction(
                label='Off',
                text='Light off'
            )
        ]
    )
)

# ��ͧ�ѵ������§ ����ҹ �ҡ�Ѵ�ʧ �Ѻ �Ѵ�� �ҡ�Ѵ�س�����
image_carousel_template_message2 = TemplateSendMessage(
	alt_text='ImageCarousel template',
	template=ImageCarouselTemplate(
		columns=[
			ImageCarouselColumn(
				image_url='https://i1.wp.com/www.kmusic2blog.com/wp-content/uploads/2017/02/cover.jpg',
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

buttons_template_message21 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
        title='Menu',
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

buttons_template_message22 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://pm1.narvii.com/6584/47a73dddb85c1deeff58e76a1223f6d5b12bfd0b_hq.jpg',
        title='Menu',
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

buttons_template_message3 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://img00.deviantart.net/09f6/i/2016/141/d/0/bts___the_most_beautiful_moment_in_life__yf_by_5secondsofdemi-da3a3br.jpg',
        title='Menu',
        text='Please select',
        actions=[            
            MessageTemplateAction(
                label='On',
                text='Light On'
            ),
            MessageTemplateAction(
                label='Off',
                text='Light Off'
            )
        ]
    )
)

buttons_template_message4 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i0.wp.com/www.kmusic2blog.com/wp-content/uploads/2016/10/cover-1024x1024.jpg',
        title='Menu',
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
                uri='https://www.youtube.com/watch?v=BEMaH9Sm3lQ&index=9&list=PL_Cqw69_m_yzbMVGvQA8QWrL_HdVXJQX7&t=0s'
            )
        ]
    )
)	
   
if __name__ == "__main__":
    app.run(debug=True)