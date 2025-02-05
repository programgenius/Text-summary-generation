import json

# 读取 JSON 数据
with open(r'C:\Users\Administrator\Desktop/提交.json', 'r', encoding='utf-8') as infile:
    input_data = json.load(infile)

# 处理数据并生成目标格式
output_data = []
for item in input_data:
    summary = {
        "id": item["id"],
        "summary": item["summarization"]  # 假设我们只取第一个文档的文本作为摘要
    }
    output_data.append(summary)

# 写入处理后的数据
with open(r'C:\Users\Administrator\Desktop/cinvert.json', 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print("数据处理完成，输出已保存到 convert.json")
