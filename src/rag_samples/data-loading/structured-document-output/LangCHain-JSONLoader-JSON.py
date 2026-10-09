import os

from langchain_community.document_loaders import JSONLoader

script_dir = os.path.dirname(__file__)
print(f"获取当前脚本文件所在的目录：{script_dir}")
file_dir = os.path.join(script_dir, '../../data/灭神纪/人物角色.json')
print(f"获取文件的目录：{file_dir}")

print("=== JSONLoader 加载结果 ===")
print("1. 主角信息：")
json_loader = JSONLoader(file_path=file_dir, jq_schema='.mainCharacter | "姓名：" + .name + "，背景：" + .backstory',
                         text_content=True)
json_char = json_loader.load()
print(json_char)

print("\n2. 支持角色信息：")
support_loader = JSONLoader(
    file_path=file_dir,
    jq_schema='.supportCharacters[] | "姓名：" + .name + "，背景：" + .background',
    text_content=True
)

supper_char = support_loader.load()
print(supper_char)
