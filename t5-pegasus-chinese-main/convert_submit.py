import json

def convert_format(input_data):
    output_data = []
    for line in input_data:
        summary, id_part = line.strip().rsplit('\t', 1)
        output_entry = {
            "id": id_part,
            "summary": summary
        }
        output_data.append(output_entry)
    return output_data

def main():
    # 输入文件路径
    input_file_path = r'C:\Users\Administrator\Desktop\output.tsv'
    # 输出文件路径
    output_file_path = r'C:\Users\Administrator\Desktop\result.json'

    # 从输入文件读取数据
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_data = file.readlines()

    # 转换格式
    output_data = convert_format(input_data)

    # 自定义写入格式，确保冒号后有空格
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write('[\n')
        for i, entry in enumerate(output_data):
            file.write('    {\n')
            file.write(f'        "id": "{entry["id"]}",\n')
            file.write(f'        "summary": "{entry["summary"]}"\n')
            file.write('    }')
            if i < len(output_data) - 1:
                file.write(',\n')
            else:
                file.write('\n')
        file.write(']\n')

if __name__ == "__main__":
    main()
















# import json
#
# def convert_format(input_data):
#     output_data = []
#
#     for line in input_data:
#         summary, id_part = line.strip().rsplit('\t', 1)
#
#         output_entry = {
#             "id": id_part,
#             "summary": summary
#         }
#
#         output_data.append(output_entry)
#
#     return output_data
#
#
# def main():
#     # 输入文件路径
#     input_file_path = r'C:\Users\Administrator\Desktop/output.tsv'
#     # 输出文件路径
#     output_file_path = r'C:\Users\Administrator\Desktop/result.json'
#
#     # 从输入文件读取数据
#     with open(input_file_path, 'r', encoding='utf-8') as file:
#         input_data = file.readlines()
#
#     # 转换格式
#     output_data = convert_format(input_data)
#
#     # 将输出结果写入 JSON 文件
#     with open(output_file_path, 'w', encoding='utf-8') as json_file:
#         json.dump(output_data, json_file, ensure_ascii=False, indent=4)
#
#
# if __name__ == "__main__":
#     main()
