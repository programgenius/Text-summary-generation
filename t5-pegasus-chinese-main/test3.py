# 取文件1的id和文件2的摘要拼接

import os
import json

file1 = r'C:\Users\Administrator\Desktop/result.tsv'

# file2 = r'C:\Users\Administrator\Desktop/test2_clean.json'
file2 = r'C:\Users\Administrator\Desktop/test2_clean.json'
output = r'C:\Users\Administrator\Desktop/output.tsv'

import json

# 读取文件1的每一行
with open(file1, 'r', encoding='utf-8') as f1:
    lines = f1.readlines()

# 读取并解析文件2的JSON数据
with open(file2, 'r', encoding='utf-8') as f2:
    data = json.load(f2)

# 提取文件2中的每个ID
ids = [item['id'] for item in data]

# 确保文件1和文件2的行数相同
if len(lines) != len(ids):
    print(len(lines))
    print(len(ids))
    raise ValueError("文件1和文件2的行数不同，无法一一对应拼接。")

# 创建并输出连接后的结果
with open(output, 'w', encoding='utf-8') as output_file:
    for line, id_ in zip(lines, ids):
        line = line.strip()  # 去除每行末尾的换行符
        output_file.write(f"{line}\t{id_}\n")

print("连接完成，结果保存在 output.txt 文件中。")


