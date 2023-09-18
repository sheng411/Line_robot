from a_token import iot_token,iot_secret
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, ImageSendMessage    # 載入 TextSendMessage 和 ImageSendMessage 模組
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
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        img_url = reply_img(msg)   # 取得對應的圖片，如果沒有取得，會是 False
        if img_url:
            # 如果有圖片網址，回傳圖片
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(tk,img_message)
        else:
            # 如果是 False，回傳文字
            text_message = TextSendMessage(text='找不到相關圖片')
            line_bot_api.reply_message(tk,text_message)
    except:
        print('error')
    return 'OK'
# 建立回覆圖片的函式
def reply_img(text):
    # 文字對應圖片網址的字典
    img = {
        '皮卡丘':'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png',
        '傑尼龜':'https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png'
    }
    if text in img:
      return img[text]
    else:
      # 如果找不到對應的圖片，回傳 False
      return False

if __name__ == "__main__":
    app.run()