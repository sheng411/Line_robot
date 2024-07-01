import requests
from load_id import *
from a_token import *

# LINE 機器人的 Channel Access Token
channel_access_token = iot_token

#user list
user_ids = read_user_ids()

#"This's a test message from a group.\n\nIf you receive this message, please reply to me."
type_in=input("title(New/Update/other)-->")
text_input=input("msg->")
text=f"*{type_in}*\n{text_input}"


#message
message = {
    "type": "text",
    "text": text
}

# LINE Messaging API 的發送訊息的 API 網址
api_url = f"https://api.line.me/v2/bot/message/multicast"

# setting HTTP header
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {channel_access_token}"
}

# send POST request
response = requests.post(api_url, headers=headers, json={
    "to": user_ids,         #Send to users who are on the list
    "messages": [message]
})

# check
if response.status_code == 200:
    print("Message successfully sent\n")
    print(text,"\n")
else:
    print(f"Failed to send message,Error code:{response.status_code}\n\n")
    print(response.text)
