import time
from Li_main import *


def run_rdr():
    run_time = time.localtime()
    h=run_time.tm_hour
    m=run_time.tm_min
    s=run_time.tm_sec
    h_min=15
    h_max=23
    m_time=0
    s_time=1
    if (h>=h_min and h<=h_max) and m==m_time and s==s_time:
        rd_run()
        print("rd ok")

def rd_run():
    current_time = time.localtime()
    lt=time.strftime("%Y/%m/%d  %H:%M:%S",current_time)
    
    radar_url = rd_url
    radar = requests.get(radar_url)
    radar_json = radar.json()
    radar_img = radar_json['cwaopendata']['dataset']['resource']['ProductURL']
    radat_time = radar_json['cwaopendata']['dataset']['DateTime']   # 取得時間
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

while True:
    run_rdr()
    time.sleep(0.5)