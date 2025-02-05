import re
import json

# 查找缺少的id

# 从文件1中提取ID
def extract_ids_from_file1(file1_path):
    ids_file1 = set()
    with open(file1_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            if "id" in entry:
                ids_file1.add(entry["id"])
    return ids_file1

# 从文件2中提取ID
def extract_ids_from_file2(file2_path):
    ids_file2 = set()  #集合的差集运算
    with open(file2_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            if "id" in entry:
                ids_file2.add(entry["id"])
    return ids_file2

# 找出文件1中缺失的ID
def find_missing_ids(file1_ids, file2_ids):
    missing_ids = file2_ids - file1_ids
   
    return missing_ids

# 路径设置
file1_path = r'C:\Users\Administrator\Desktop/test2.json'
file2_path = r'C:\Users\Administrator\Desktop/test2_clean.json'

# 提取ID
file1_ids = extract_ids_from_file1(file1_path)
file2_ids = extract_ids_from_file2(file2_path)

# 找出文件1中缺失的ID
missing_ids = find_missing_ids(file1_ids, file2_ids)

# 输出结果
print("文件1中缺失的ID:", missing_ids)
