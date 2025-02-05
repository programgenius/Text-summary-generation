# 查找 summarization为空的
import json

# 打开 JSON 文件并读取数据
with open('C:/Users/Administrator/Desktop/f.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历列表中的每个字典
for entry in data:
    # 获取 summarization
    summarization = entry.get('summarization')

    # 检查 summarization 是否为空或 None
    if summarization is None or summarization.strip() == "":
        # 打印出对应的 id
        print("Error in summarization for ID:", entry.get('id'))
