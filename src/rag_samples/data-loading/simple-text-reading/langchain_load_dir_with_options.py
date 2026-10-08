import os

from langchain_community.document_loaders import DirectoryLoader

script_dir = os.path.dirname(__file__)
print(f"获取当前脚本文件所在的目录：{script_dir}")
file_dir = os.path.join(script_dir, '../../data/黑悟空')
print(f"获取文件的目录：{file_dir}")

loader = DirectoryLoader(
    file_dir,
    glob="**/*.md",
    use_multithreading=True,
    show_progress=True
)
docs = loader.load()

print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])  # 输出第一个文档
