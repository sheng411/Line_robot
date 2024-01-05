file_path='Linebot_iot/user_id.txt'

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
        print(f"找不到檔案: {file_path}")

    return user_ids

# 使用範例
user_ids_list = read_user_ids()
print("User IDs List:", user_ids_list)
