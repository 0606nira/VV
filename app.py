from flask import Flask, request, abort

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
 #RichMenu, RichMenuArea, RichMenuBound,
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
	#message = event.message.text
	try:
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='TaeTae Luv U'))
    
	except linebot.exceptions.LineBotApiError as e:
		print(e.status_code)
		print(e.error.message)
		print(e.error.details)

if __name__ == "__main__":
	app.run(debug=True)