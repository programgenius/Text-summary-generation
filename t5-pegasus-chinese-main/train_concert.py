
import json
import os

# 读取 JSON 文件
input_file = 'C:/Users/Administrator/Desktop/f.json'  # 输入文件名
output_file = 'C:/Users/Administrator/Desktop/f.tsv'  # 输出文件名

# 检查输入文件是否存在
if not os.path.exists(input_file):
    print(f"输入文件未找到: {input_file}")
else:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)  # 确保加载为字典


    # 遍历每个条目
    output_lines = []
    for entry in data:
        summarization = entry['summarization']
        doc_texts = [doc['text'].replace('\n', '') for doc in entry['documents']]
        all_text = ''.join(doc_texts)

        # 拼接ID和文本
        output_line = f"{summarization}\t{all_text}"
        output_lines.append(output_line)

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')

    print(f"数据已成功转换并写入 {output_file}")













# # 读取 JSON 文件
# input_file = 'C:/Users/Administrator/Desktop/train_clean.json’                                                                                                                       clean/valid_clean.json'  # 输入文件名
# output_file = 'C:/Users/Administrator/Desktop/train_clean——ZT.tsv'  # 输出文件名
#
# with open(input_file, 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# # 遍历每个条目
# output_lines = []
# for entry in data:
#     summarization = entry['summarization']
#     doc_texts = [doc['text'].replace('\n', '') for doc in entry['documents']]
#     all_text = ''.join(doc_texts)
#
#     # 拼接ID和文本
#     output_line = f"{summarization}\t{entry['id']}{all_text}"
#     output_lines.append(output_line)
#
# # 将结果写入输出文件
# with open(output_file, 'w', encoding='utf-8') as f:
#     for line in output_lines:
#         f.write(line + '\n')
#
# print(f"数据已成功转换并写入 {output_file}")
