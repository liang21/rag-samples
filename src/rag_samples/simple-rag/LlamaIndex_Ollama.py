import os
from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

# 加载配置文件
load_dotenv()

# 创建Ollama嵌入模型
embed_model = OllamaEmbedding(model_name="qwen3-embedding:latest")
# 创建Ollama LLM
llm = Ollama(model=os.environ["OLLAMA_MODEL"], request_timeout=300.0)

# 加载数据
data_file = Path(__file__).resolve().parents[1] / "data" / "黑悟空" / "设定.txt"
documents = SimpleDirectoryReader(input_files=[str(data_file)]).load_data()

# 建立索引
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = index.as_query_engine(llm=llm)
print(query_engine.query("黑神话悟空中有哪些战斗工具?"))
