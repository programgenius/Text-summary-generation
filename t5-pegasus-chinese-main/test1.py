#-*- coding: utf-8 -*-

# 据路撒撒比德卡白色的接口bask觉得bask觉得被那个覅u老师的步伐
# 生成F:\t5-pegasus-chinese-main\data\predict_result4.tsv




import json

def convert_format_from_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        input_data = json.load(file)

    # 确保输入数据是一个列表
    if not isinstance(input_data, list) or len(input_data) == 0:
        raise ValueError("Input data should be a non-empty list")

    output_lines = []
    for entry in input_data:
        # 提取 id
        main_id = entry.get("id")

        # 确保 documents 存在且是一个列表
        documents = entry.get("documents")
        if not isinstance(documents, list):
            raise ValueError("documents should be a list")

        # 拼接所有的 text
        combined_text = ""
        for doc in documents:
            if isinstance(doc, dict) and "text" in doc:
                text = doc.get("text", "")
                # 去除换行符、回车符、制表符等
                text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
                combined_text += text

        # 格式化输出字符串为所需格式   变量嵌入字符串
        output_line = f'{combined_text}'
        output_lines.append(output_line)

    # 将所有格式化字符串组合成多行文本
    return "\n".join(output_lines)


def main():
    # 指定你的输入文件路径
    file_path = r'C:\Users\Administrator\Desktop/test2.json'  # 请替换为你的文件路径

    # 转换格式
    output_data = convert_format_from_file(file_path)

    # 打印输出结果
    print(output_data)

    # 写入文件，每行对应一个 id 的内容
    with open('C:/Users/Administrator/Desktop/test2.tsv', 'w', encoding='utf-8') as file:
        file.write(output_data)


if __name__ == "__main__":
    main()
































#
#
#
# import re
# import json
#
# def convert_format_from_file(file_path):
#     # 读取文件内容
#     with open(file_path, 'r', encoding='utf-8') as file:
#         input_data = json.load(file)
#
#     # 确保输入数据是一个列表
#     if not isinstance(input_data, list) or len(input_data) == 0:
#         raise ValueError("Input data should be a non-empty list")
#
#     output_lines = []
#     for entry in input_data:
#         # 提取 id
#         main_id = entry.get("id")
#
#         # 确保 documents 存在且是一个列表
#         documents = entry.get("documents")
#         if not isinstance(documents, list):
#             raise ValueError("documents should be a list")
#
#         # 拼接所有的 text  ！！！
#         # combined_text = "".join(doc.get("text", "").replace("\n", "") for doc in documents if isinstance(doc, dict) and "text" in doc)
#
#         # combined_text = "".join(
#         #     re.sub(r'\s+', ' ', doc.get("text", "")) for doc in documents if isinstance(doc, dict) and "text" in doc).strip()
#
#         combined_text = ""
#         for doc in documents:
#             if isinstance(doc, dict) and "text" in doc:
#                 text = doc.get("text", "")
#                 # 去除换行符、回车符、制表符
#                 text = text.replace("\n", "").replace("\r", "").replace("\t", "")
#                 combined_text += text
#
#         # 格式化输出字符串为所需格式
#         output_line = f'"""id"": ""{main_id}""{combined_text}'
#         output_lines.append(output_line)
#
#     # 将所有格式化字符串组合成多行文本
#     return "\n".join(output_lines)
#
#
# def main():
#     # 指定你的输入文件路径
#     file_path = r'G:\clean/test1_clean.json'  # 请替换为你的文件路径
#
#     # 转换格式
#     output_data = convert_format_from_file(file_path)
#
#     # 打印输出结果
#     print(output_data)
#
#     # 写入文件，每行对应一个 id 的内容
#     with open('C:/Users/Administrator/Desktop/test_clean_TP.tsv', 'w', encoding='utf-8') as file:
#         file.write(output_data)
#
#
# if __name__ == "__main__":
#     main()
