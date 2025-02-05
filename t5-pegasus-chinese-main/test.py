import re

def remove_id_content(text):
    # 使用正则表达式匹配 "id" 字段及其后的所有内容
    pattern = r'("""id"":\s*""""(.*?)"""(?:.*?\n?)'
    cleaned_text = re.sub(pattern, r'\1\n', text)
    return cleaned_text.strip()

def process_file(input_file, output_file):
    # 从输入文件读取内容
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # 处理文本
    output_text = remove_id_content(text)

    # 将输出写回到输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(output_text)

# 示例使用
input_filename = r'F:\t5-pegasus-chinese-main\data\predict_result.tsv'  # 输入文件名
output_filename = r'F:\t5-pegasus-chinese-main\data\predict_result.tsv'  # 输出文件名

# 调用处理文件的函数
process_file(input_filename, output_filename)

# 输出结果
print(f"处理完成，结果已写入 {output_filename}")
