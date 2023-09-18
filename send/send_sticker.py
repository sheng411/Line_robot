from a_token import iot_token,iot_secret
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import StickerSendMessage   # 載入 StickerSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi(iot_token)
        handler = WebhookHandler(iot_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']      # 取得 reply token
        stickerId = json_data['events'][0]['message']['stickerId'] # 取得 stickerId
        packageId = json_data['events'][0]['message']['packageId'] # 取得 packageId
        sticker_message = StickerSendMessage(sticker_id=stickerId, package_id=packageId) # 設定要回傳的表情貼圖
        line_bot_api.reply_message(tk,sticker_message)  # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    app.run()