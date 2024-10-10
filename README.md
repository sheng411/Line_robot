# Line_bot
常因為要查詢資料而開一堆網頁，費時又效率低，因此想透過LINE BOT及爬蟲的方式將常使用的資訊整合至機器人內，並透過關鍵字的方式快速的獲得所需要的資料。  
  
Line name:全能喵管家  
Line ID:@195ygcba  
  
參考網址:[LINE BOT教學](https://steam.oxxostudio.tw/category/python/example/line-bot.html)
# 列表
- [架構圖](https://github.com/sheng411/Line_robot?tab=readme-ov-file#%E6%9E%B6%E6%A7%8B%E5%9C%96)
- [目的](https://github.com/sheng411/Line_robot?tab=readme-ov-file#%E7%9B%AE%E7%9A%84)
- [支援列表](https://github.com/sheng411/Line_robot?tab=readme-ov-file#%E6%94%AF%E6%8F%B4%E5%88%97%E8%A1%A8)
  - [地震資訊](https://github.com/sheng411/Line_robot?tab=readme-ov-file#-%E5%9C%B0%E9%9C%87%E8%B3%87%E8%A8%8A)
  - [雷達回波圖](https://github.com/sheng411/Line_robot?tab=readme-ov-file#-%E9%9B%B7%E9%81%94%E5%9B%9E%E6%B3%A2%E5%9C%96)
  - [下週油價](https://github.com/sheng411/Line_robot?tab=readme-ov-file#-%E4%B8%8B%E9%80%B1%E6%B2%B9%E5%83%B9)


# 架構圖
![image](https://github.com/user-attachments/assets/6f48ad67-9168-4b01-a2e7-6669062262ef)

# 目的
透過LINE bot創造出符合自己需求的機器人。

# 支援列表
目前所支援的的功能如下:  
### -地震資訊  
>大地震(可檢視顯著有感地震)
>>範例: 輸入**地震資訊** 或 **地震** 點選**大地震**
>>![S__29384727](https://github.com/user-attachments/assets/84ccde55-b880-411f-b7c9-d35fe9a3ff00)
>小地震(可檢視小規模區域地震)
>>範例: 輸入**地震資訊** 或 **地震** 點選**小地震**
>>![S__29384732](https://github.com/user-attachments/assets/8635264d-dd91-41d9-8245-6720053d0346)

### -雷達回波圖  
>抓取中央氣象署API資料進行分析，取得近10分鐘雷達回波圖影像。
>>範例: 輸入**雷達回波** 或 **雷達回波圖**
![S__29384711](https://github.com/user-attachments/assets/46fbe11a-c6a3-47b1-936e-58c560e1b783)


### -下週油價  
>*因抓取的資料為臺灣中油官方網站資料(皆為週日更新下週資訊)，故無法像新聞提前幾天取得下週油價資訊*
>>範例: 輸入**油價** 點選**92無鉛**
![S__29384715](https://github.com/user-attachments/assets/141c477f-7667-4781-99a4-63d5348fb166)

