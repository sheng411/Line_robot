import json

json_data ={}#{'destination': 'Uc70b27a36f076c509e7a487e26a5f756', 'events': [{'type': 'message', 'message': {'type': 'text', 'id': '489227869973643270', 'quoteToken': 'wXzZiOFhkADF6Cw56HAS7Dnu4ij9b5MvJTbRx5oLOGSGDl1rBk1ULRiNnZreGMXusAy490N6IdsimqKt9dQXgSx_jRh4U5omk-ldFbZM1ZYLc8iMA7MdaVd83OrY6jS-7-aFalop-S5VGsWTFJWy-g', 'text': '雷達回波圖'}, 'webhookEventId': '01HKC2RTEH95N3E4ZBM4VJ6VK1', 'deliveryContext': {'isRedelivery': False}, 'timestamp': 1704433838232, 'source': {'type': 'user', 'userId': 'Uf48f0ce5840bd06db633ef9a3202e2d1'}, 'replyToken': '6b3b20341ebd403088a231ac714991c8', 'mode': 'active'}]}
file_path='Linebot_iot/user_id.txt'


def write_userid_file(json_data):
    user_id = json_data['events'][0]['source']['userId']
    print("get id")
    try:
        # 讀取現有的 user_ids
        existing_user_ids = read_user_ids()

        # 判斷是否已經存在
        if user_id not in existing_user_ids:
            # 寫入 user_id.txt 檔案
            with open(file_path, 'a') as file:
                file.write(user_id + '\n')

            print(f'UserId {user_id} has been written to the {file_path} file,OK!!!\n')
        else:
            print(f'UserId {user_id} already exists in file {file_path} ,Skip writing\n')

    except FileNotFoundError:
        print(f"Can't find the file: {file_path}\n")

def read_user_ids():
    user_ids = []
    try:
        # 開啟檔案並讀取每一行
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # 將每一行的 userId 加入到 user_ids 中
            for line in lines:
                user_ids.append(line.strip())  # 移除換行符號

    except FileNotFoundError:
        print(f"找不到檔案: {file_path}\n")

    return user_ids

# 使用範例(測試用)
'''
user_id = json_data['events'][0]['source']['userId']
write_userid_file(json_data)
'''