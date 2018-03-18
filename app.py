import json
import requests
from flask import Flask, request
app = Flask(__name__)
global Authorization
Authorization = 'Bearer MEMIUEV7R2dzmxXVTkQRcgply61mFF16A/BEXFbh01XuuN1oGwhLH5t+GbxcJRIXEsiioQe7xhs0mluGITwfR55jRSRsd3R+JTBz6Z1O3Q+Ei0OIYS2QT0Mg86n6UZowtp0nO7HWmJBQJoCc4nSyMgdB04t89/1O/w1cDnyilFU='
@app.route('/')
def index():
  return "Hello World!"

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST'])
def callback():
  json_line = request.get_json()
  json_line = json.dumps(json_line)
  decoded = json.loads(json_line)
  user = decoded["events"][0]['replyToken']
  #id=[d['replyToken'] for d in user][0]
  #print(json_line)
  print("user:", user)
  sendMes()
  #sendText(user,'Lovely') 
  return '',200


def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/richmenu'
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization':Authorization
  }
  data = json.dumps({
  "replyToken":user,
  "messages":[{"type":"text","text":text}]})
  
  #print("ข้อมูล:",data)
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
  #print(r.text)

def sendMes():
	message = json.dumps['events'][0]['message']['text']
	if(message == 'Hi'):
		sendText(user, 'Just Sleep')
	else:
		sendText(user, 'Go to BED')

if __name__ == '__main__':
  app.run(debug=True)