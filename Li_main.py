from a_token import *
from a_location import locat
from a_img import img
from a_msg import msg
from flask import Flask, request
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage,PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate
import requests,time,statistics

'''
若有新增資訊都需要重新執行
'''

app = Flask(__name__)
text_ck=0

@app.route("/", methods=['POST'])
def linebot():
    global text_ck,userid,reply_token
    try:
        body = request.get_data(as_text=True)
        json_data = json.loads(body)                           # json 格式化收到的訊息
        print("\n\n\n",json_data,"\n\n\n")
        line_bot_api = LineBotApi(iot_token)
        handler = WebhookHandler(iot_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']       # 取得 reply token
        tp = json_data['events'][0]['message']['type']  # 取得 message 的類型
        reply_token = json_data['events'][0]['replyToken'] # 取得回傳訊息的 Token ( reply message 使用 )

        if json_data['events'][0]['source']['type'] =="group":  #判斷是從群組/個人傳送
            print("group!!")
            userid = json_data['events'][0]['source']['groupId']  # 取得 userid
        else:
            userid = json_data['events'][0]['source']['userId']  # 取得 userid

        if 'message' in json_data['events'][0]:
            if json_data['events'][0]['message']['type'] == 'location':
                address = json_data['events'][0]['message']['address'].replace('台','臺')
                # 回覆爬取到的相關氣象資訊
                reply_msg(f'{address}\n\n{current_weather(address)}', reply_token, access_token)
                print(address)

        if tp == 'text':
            # 如果是文字類型的訊息
            msg = check_msg(json_data['events'][0]['message']['text'])   # 取出文字並對應到 reply_msg 的函式
            if msg[0] == 'text':
                msg_ck(msg[1])
                '''
                if msg[1]=="資訊面板":
                    temp_msg()
                elif msg[1]=="雷達回波" or msg[1]=="雷達回波圖":
                    rd_run()
                elif msg[1]=="小地震" or msg[1]=="小地震資訊":
                    earth(s_earth_jurl)
                elif msg[1]=="大地震" or msg[1]=="大地震資訊":
                    earth(b_earth_jurl)
                else:

                '''
                # 如果要回傳的訊息是 text，使用 TextSendMessage 方法
                if text_ck==0:
                    msg[1]="你傳的是:"+msg[1]
                if text_ck==1:
                    msg[1]=msg[1]
                    line_bot_api.reply_message(tk,TextSendMessage(text=msg[1]))
                text_ck=0
            if msg[0] == 'location':
                # 如果要回傳的訊息是 location，使用 LocationSendMessage 方法
                line_bot_api.reply_message(tk,LocationSendMessage(title=msg[1]['title'],
                                                                address=msg[1]['address'],
                                                                latitude=msg[1]['latitude'],
                                                                longitude=msg[1]['longitude']))
            if msg[0] == 'image':
                # 如果要回傳的訊息是 image，使用 ImageSendMessage 方法
                line_bot_api.reply_message(tk,ImageSendMessage(original_content_url=msg[1],
                                                                preview_image_url=msg[1]))
        if tp == 'sticker':
            # 如果收到的訊息是表情貼圖
            stickerId = json_data['events'][0]['message']['stickerId'] # 取得 stickerId
            packageId = json_data['events'][0]['message']['packageId'] # 取得 packageId
            # 使用 StickerSendMessage 方法回傳同樣的表情貼圖
            line_bot_api.reply_message(tk,StickerSendMessage(sticker_id=stickerId, package_id=packageId))
        if tp == 'location':
            # 如果是收到的訊息是地點資訊
            line_bot_api.reply_message(tk,TextSendMessage(text='好地點!'))
        if tp == 'image':
            # 如果是收到的訊息是圖片
            line_bot_api.reply_message(tk,TextSendMessage(text='好圖給讚!'))
        if tp == 'audio':
            # 如果是收到的訊息是聲音
            line_bot_api.reply_message(tk,TextSendMessage(text='天籟天籟'))
        if tp == 'video':
            # 如果是收到的訊息是影片
            line_bot_api.reply_message(tk,TextSendMessage(text='影片內容真是不錯!'))
    except:
        print('error', body)
    return 'OK'

# 定義回覆訊息的函式
def check_msg(text):
    global text_ck
    # 預設回覆的文字就是收到的訊息
    reply_msg_content = ['text',text]
    if text in msg:
        reply_msg_content = ['text',msg[text.lower()]]
        text_ck=1
    if text in locat:
        reply_msg_content = ['location',locat[text.lower()]]
        text_ck=1
    if text in img:
        reply_msg_content = ['image',img[text.lower()]]
        text_ck=1
    return reply_msg_content


def msg_ck(m):
    global text_ck
    print("m-->",m)
    if m=="資訊面板":
        temp_msg()
        text_ck=2
        print("資訊_ok")
    if m=="地震資訊" or m=="地震":
        earth_temp_msg()
        text_ck=2
        print("地震資訊_ok")
    if m=="雷達回波" or m=="雷達回波圖":
        rd_run()
        text_ck=2
        print("rd_ok")
    if m=="小地震" or m=="小地震資訊":
        earth(s_earth_jurl)
        text_ck=2
        print("小地震_ok")
    if m=="大地震" or m=="大地震資訊":
        earth(b_earth_jurl)
        text_ck=2
        print("大地震_ok")

#資訊介面
def temp_msg():
    line_bot_api = LineBotApi(iot_token)
    line_bot_api.push_message(iot_userid, TemplateSendMessage(
    alt_text='資訊介面',
    template=ButtonsTemplate(
        thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
        title='我還沒想到要用什麼',
        text='這是按鈕樣板',
        actions=[
            PostbackAction(
                label='postback',
                data='temp_test'
            ),
            MessageAction(
                label='我可以幹嘛?',
                text='help'
            ),
            URIAction(
                label='不要點這個網址',
                uri='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            ),
            URIAction(
                label='node-red儀表板',
                uri='http://140.127.196.119:18815/ui/#!/0?socketid=0chTv_64rh4pFhuyAAAr'
            )
        ]
    )
))

#地震資訊介面
def earth_temp_msg():
    line_bot_api = LineBotApi(iot_token)
    line_bot_api.push_message(userid, TemplateSendMessage(
    alt_text='地震資訊',
    template=ButtonsTemplate(
        thumbnail_image_url='https://d1j71ui15yt4f9.cloudfront.net/wp-content/uploads/2022/09/18001312/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2-2022-09-18-001145-786x1024.jpg',
        title='地震資訊',
        text='點選下方按鈕選擇想看到的地震資訊',
        actions=[
            MessageAction(
                label='小地震資訊',
                text='小地震'
            ),
            MessageAction(
                label='大地震資訊',
                text='大地震'
            ),
        ]
    )
))

#雷達回波圖
def rd_run():
    current_time = time.localtime()
    lt=time.strftime("%Y/%m/%d  %H:%M:%S",current_time)
    
    radar_url = rd_url
    radar = requests.get(radar_url)
    radar_json = radar.json()
    radar_img = radar_json['cwaopendata']['dataset']['resource']['ProductURL']
    radat_time = radar_json['cwaopendata']['dataset']['DateTime']   # 取得時間
    
    '''
    print(radar_img)
    token = notify_token
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message':'\n雷達回波圖\n'+str(lt),
        'imageThumbnail':radar_img + '?' + radat_time,    # 加上時間參數
        'imageFullsize':radar_img + '?' + radat_time      # 加上時間參數
    }
    data = requests.post(l_notify_url, headers=headers, data=data)
    '''
    
    #push
    headers = {
        'Authorization':'Bearer '+iot_token,
        'Content-Type':'application/json'
    }

    #reply text
    body = {
        'replyToken':reply_token,
        'messages':[{
                'type': 'text',
                'text':'雷達回波圖\n'+str(lt)
            }]
    }
    
    #push img
    ibody = {
        'to':userid,
        'messages':[{
            'type': 'image',
            'originalContentUrl': radar_img+ '?' + radat_time,
            'previewImageUrl': radar_img+ '?' + radat_time
            }]
        }
    req = requests.request('POST', l_reply_url,headers=headers,data=json.dumps(body).encode('utf-8'))
    ireq = requests.request('POST', l_push_url,headers=headers,data=json.dumps(ibody).encode('utf-8'))
    #print(req.text)
    
    print(lt,"rd push ok")

#地震資訊
def earth(url):
    data = requests.get(url)
    data_json = data.json()
    eq = data_json['records']['Earthquake']    # 轉換成 json 格式
    for i in eq:
        loc = i['EarthquakeInfo']['Epicenter']['Location']        # 地震地點
        val = i['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue']  # 芮氏規模
        dep = i['EarthquakeInfo']['FocalDepth']               # 地震深度
        eq_time = i['EarthquakeInfo']['OriginTime']               # 地震時間
        #print(f'地震發生於{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}')
        img = i['ReportImageURI']
        msg = f'{loc}\n芮氏規模 {val} 級\n深度 {dep} 公里\n發生時間 {eq_time}'
        '''
        token = notify_token 
        headers = {
            'Authorization': 'Bearer ' + token      # POST 使用的 headers
        }
        data = {
            'message':msg,            # 發送的訊息
            'imageThumbnail':img,     # 預覽圖網址
            'imageFullsize':img       # 完整圖片網址
        }
        data = requests.post(l_notify_url, headers=headers, data=data)    # 發送 LINE NOtify
        '''
        #push data
        push_msg(img)
        reply_msg(msg)

        break


# 目前天氣函式
def current_weather(address):
    city_list, area_list, area_list2 = {}, {}, {} # 定義好待會要用的變數
    msg = '找不到氣象資訊。'                         # 預設回傳訊息

    # 定義取得資料的函式
    def get_data(url):
        w_data = requests.get(url)   # 爬取目前天氣網址的資料
        w_data_json = w_data.json()  # json 格式化訊息內容
        location = w_data_json['cwbopendata']['location']  # 取出對應地點的內容
        for i in location:
            name = i['locationName']                       # 測站地點
            city = i['parameter'][0]['parameterValue']     # 縣市名稱
            area = i['parameter'][2]['parameterValue']     # 鄉鎮行政區
            temp = check_data(i['weatherElement'][3]['elementValue']['value'])                       # 氣溫
            humd = check_data(round(float(i['weatherElement'][4]['elementValue']['value'] )*100 ,1)) # 相對濕度
            r24 = check_data(i['weatherElement'][6]['elementValue']['value'])                        # 累積雨量
            if area not in area_list:
                area_list[area] = {'temp':temp, 'humd':humd, 'r24':r24}  # 以鄉鎮區域為 key，儲存需要的資訊
            if city not in city_list:
                city_list[city] = {'temp':[], 'humd':[], 'r24':[]}       # 以主要縣市名稱為 key，準備紀錄裡面所有鄉鎮的數值
            city_list[city]['temp'].append(temp)   # 記錄主要縣市裡鄉鎮區域的溫度 ( 串列格式 )
            city_list[city]['humd'].append(humd)   # 記錄主要縣市裡鄉鎮區域的濕度 ( 串列格式 )
            city_list[city]['r24'].append(r24)     # 記錄主要縣市裡鄉鎮區域的雨量 ( 串列格式 )

    # 定義如果數值小於 0，回傳 False 的函式
    def check_data(e):
        return False if float(e)<0 else float(e)

    # 定義產生回傳訊息的函式
    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address: # 如果地址裡存在 key 的名稱
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]['temp'] != False else ''
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]['humd'] != False else ''
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]['r24'] != False else ''
                description = f'{temp}{humd}{r24}'.strip('，')
                a = f'{description}。' # 取出 key 的內容作為回傳訊息使用
                break
        return a

    try:
        get_data(weather_1_url)
        get_data(weather_2_url)

        for i in city_list:
            if i not in area_list2: # 將主要縣市裡的數值平均後，以主要縣市名稱為 key，再度儲存一次，如果找不到鄉鎮區域，就使用平均數值
                area_list2[i] = {'temp':round(statistics.mean(city_list[i]['temp']),1),
                                'humd':round(statistics.mean(city_list[i]['humd']),1),
                                'r24':round(statistics.mean(city_list[i]['r24']),1)
                                }
        msg = msg_content(area_list2, msg)  # 將訊息改為「大縣市」
        msg = msg_content(area_list, msg)   # 將訊息改為「鄉鎮區域」
        return msg    # 回傳 msg
    except:
        return msg    # 如果取資料有發生錯誤，直接回傳 msg

#push message function
def push_msg(img):
    headers = {
        'Authorization':'Bearer '+iot_token,
        'Content-Type':'application/json'
    }

    #push img
    ibody = {
        'to':userid,
        'messages':[{
            'type': 'image',
            'originalContentUrl':img,
            'previewImageUrl':img
            }]
        }
    ireq = requests.request('POST', l_push_url,headers=headers,data=json.dumps(ibody).encode('utf-8'))

#reply message function
def reply_msg(msg):
    headers = {
        'Authorization':'Bearer '+iot_token,
        'Content-Type':'application/json'
    }

    #reply text
    body = {
        'replyToken':reply_token,
        'messages':[{
                'type': 'text',
                'text':msg
            }]
    }
    req= requests.request('POST', l_reply_url,headers=headers,data=json.dumps(body).encode('utf-8'))


if __name__ == "__main__":
    app.run()