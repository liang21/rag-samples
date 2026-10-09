import os.path

from langchain_community.document_loaders import TextLoader

script_dir = os.path.dirname(__file__)
print(f"获取当前脚本文件所在的目录：{script_dir}")
file_dir = os.path.join(script_dir,'../../data/黑悟空/设定.txt')
print(f"获取文件的目录：{file_dir}")
loader = TextLoader(file_dir)

documents = loader.load()

print(documents)
