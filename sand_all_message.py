import requests
from load_id import *
from a_token import *

# LINE 機器人的 Channel Access Token
channel_access_token = iot_token

#user list
user_ids = read_user_ids()

#"This's a test message from a group.\n\nIf you receive this message, please reply to me."
text="*update*\n工程師已將雷達回波圖已完成搶修,還順便休息一下."

# 訊息內容
message = {
    "type": "text",
    "text": text
}

# LINE Messaging API 的發送訊息的 API 網址
api_url = f"https://api.line.me/v2/bot/message/multicast"

# 設定 HTTP 標頭
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {channel_access_token}"
}

# 發送 POST 要求
response = requests.post(api_url, headers=headers, json={
    "to": user_ids,         #Send to users who are on the list
    "messages": [message]
})

# 檢查是否成功
if response.status_code == 200:
    print("訊息已成功發送\n")
    print(text,"\n")
else:
    print(f"發送訊息失敗，錯誤碼：{response.status_code}\n\n")
    print(response.text)
