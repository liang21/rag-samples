import os

from langchain_community.document_loaders import TextLoader

script_dir = os.path.dirname(__file__)
print(f"获取当前脚本文件所在的目录：{script_dir}")
file_dir = os.path.join(script_dir, '../../data/灭神纪/人物角色.json')
print(f"获取文件的目录：{file_dir}")

print("=== TextLoader 加载结果 ===")

loader = TextLoader(file_dir)
text_documents = loader.load()

print(text_documents)
