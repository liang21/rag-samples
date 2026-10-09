import os

from llama_index.core import SimpleDirectoryReader

script_dir = os.path.dirname(__file__)
print(f"获取当前脚本文件所在的目录：{script_dir}")
file_dir = os.path.join(script_dir, '../../data/黑悟空')
print(f"获取文件的目录：{file_dir}")

dir_reader = SimpleDirectoryReader(file_dir)
docs = dir_reader.load_data()

# 查看加载的文档数量和内容
print(f"文档数量: {len(docs)}")
print(docs[0].text[:100])  # 打印第一个文档的前100个字符

# 紧加载一个配置文件
dir_path = file_dir + "/设定.txt"
reader = SimpleDirectoryReader(input_files=[dir_path])
data = reader.load_data()
print(f"文档数量: {len(data)}")
print(data[0].text[:100])  # 打印第一个文档的前100个字符