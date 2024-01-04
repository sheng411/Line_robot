import json

packet_content = {}

def write_user_id_to_file(user_id, file_path='user_id.txt'):
    try:
        # 讀取現有的 user_ids
        existing_user_ids = read_user_ids(file_path)

        # 判斷是否已經存在
        if user_id not in existing_user_ids:
            # 寫入 user_id.txt 檔案
            with open(file_path, 'a') as file:
                file.write(user_id + '\n')

            print(f'UserId {user_id} 已寫入 {file_path} 檔案中\n')
        else:
            print(f'UserId {user_id} 已存在於 {file_path} 檔案中,將略過寫入\n')

    except FileNotFoundError:
        print(f"找不到檔案: {file_path}\n")

def read_user_ids(file_path='user_id.txt'):
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

# 使用範例
user_id = packet_content['events'][0]['source']['userId']
write_user_id_to_file(user_id)
