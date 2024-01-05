#   It's an automated program that crawls CPC oil prices.   #

'''
Releases   0.1
modify time:    2024/01/04

'''


import requests
import re
import json

oil_prices=[]
oil_new_time=[]
difference=0

def CPC_oil_prices():
    url = "https://www.cpc.com.tw/historyprice.aspx?n=2890"

    resp = requests.get(url)
    m = re.search("var pieSeries = (.*);", resp.text)
    jsonstr = m.group(0).strip('var pieSeries = ').strip(";")
    j = json.loads(jsonstr)
    #print(j)

    for item in reversed(j):
        for data in item['data']:
            if data['name']=="95 無鉛汽油":
                oil_prices.append(data['y'])
                oil_new_time.append(item['name'])
    #print("oil-->",oil_prices)
    #print(oil_new_time)
    difference=oil_prices[0]-oil_prices[1]
    
    if difference>0:
        msg=f"最新一筆資料時間\n{oil_new_time[0]}\n\n95無鉛汽油: {oil_prices[0]}\n\n*油價上漲*, 漲幅: {round(abs(difference), 1)}"
        return msg
    elif difference<0:
        msg=f"最新一筆資料時間\n{oil_new_time[0]}\n\n95無鉛汽油: {oil_prices[0]}\n\n*油價下跌*, 跌幅: {round(abs(difference), 1)}"
        return msg
        #return "\noil down",round(abs(difference), 1),"\nLatest Information Time->",oil_new_time[0]
    else:
        return f"最新一筆資料時間\n{oil_new_time[0]}\n\n95無鉛汽油: {oil_prices[0]}\n\n*油價不變動*{round(abs(difference), 1)}"
    return msg

#print(CPC_oil_prices())

'''
for item in reversed(j):
    for data in item['data']:
        if data['name']=="95 無鉛汽油":
            print("date:" + item['name'])
            print(data['name'] + ":" + str(data['y']))
            print("======")
'''