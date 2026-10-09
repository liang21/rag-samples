import os

from langchain_community.document_loaders import UnstructuredMarkdownLoader

script_dir = os.path.dirname(__file__)
print(f"获取当前脚本文件所在的目录：{script_dir}")
file_dir = os.path.join(script_dir, '../../data/黑悟空/黑悟空版本介绍.md')
print(f"获取文件的目录：{file_dir}")

loader = UnstructuredMarkdownLoader(file_dir)
data = loader.load()

print(data[0].page_content[:250])

markdown_loader = UnstructuredMarkdownLoader(file_dir, mode="elements")
markdown_data = markdown_loader.load()

print(f"Number of documents: {len(data)}\n")
for document in data:
    print(f"{document}\n")

