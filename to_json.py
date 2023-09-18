import json
from datetime import datetime
import os
import ast

output_folder = r"./json"

unformatted_json= input("-->")
my_dict = ast.literal_eval(unformatted_json)

formatted_json = json.dumps(my_dict, indent=2, ensure_ascii=False)

current_date = datetime.now().strftime("%m-%d__%H-%M-%S")

output_file_name = f"{current_date}.json"

output_file_path = os.path.join(output_folder, output_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(output_file_path, 'w', encoding='utf-8') as outfile:
    outfile.write(formatted_json)

print(f"\n\njson OK {output_file_name}\n\n")

