from flask import Flask, request, abort

import antolib

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

# username of anto.io account
user = 'Nira'

# key of permission, generated on control panel anto.io
key = 'WNS3El4QsXI2cZe3FbA9Nj72UO70HaN6i2RpKVDU'

# your default thing.
thing = 'Flower'

anto = antolib.Anto(user, key, thing)

def connectedCB():
    anto.sub("LED1");
    anto.sub("LED2");

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

	if(message == 'LED1 On'):
		anto.pub('LED1', 1)
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text='Light On at Bedroom'))
	elif(message == 'LED1 Off'):
		anto.pub('LED1', 0)
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text='Light Off at Bedroom'))
			
def dataCB(channel, msg):
	#message = event.message.text
	to = 'U5db26ce3aad1c4d83691ea5d6992116a'
	if(channel == 'LED1'):
		value = int(msg)
		if(value == 1):
			line_bot_api.push_message(
			to, 
			TextSendMessage(text='Light on at Bedroom'))
		else:
			line_bot_api.push_message(
			to, 
			TextSendMessage(text='Light off at Bedroom'))
			
	elif(channel == 'LED2'):
		if(value == 1):
			line_bot_api.push_message(
			to, 
			TextSendMessage(text='Light on at Storage Room'))
		else:
			line_bot_api.push_message(
			to, 
			TextSendMessage(text='Light off at Storage Room'))
			
   
if __name__ == "__main__":

	anto.mqtt.onConnected(connectedCB)
	anto.mqtt.onData(dataCB)
	anto.mqtt.connect()
	app.run(debug=True)