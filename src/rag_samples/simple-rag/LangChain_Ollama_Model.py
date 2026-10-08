import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 加载配置文件
load_dotenv()


def load_web_documents(*urls: str) -> list[Document]:
    """抓取网页正文，替代已停止维护的 langchain_community.WebBaseLoader。"""
    headers = {"User-Agent": os.getenv("USER_AGENT", "rag-samples/0.1.0")}
    documents = []
    for url in urls:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        # 维基百科正文容器，取不到时退回整页
        main = soup.select_one("#mw-content-text") or soup
        documents.append(
            Document(page_content=main.get_text(separator="\n"), metadata={"source": url})
        )
    return documents


docs = load_web_documents("https://zh.wikipedia.org/wiki/黑神话：悟空")

# 文档分块
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# 设置嵌入模型
embeddings = OllamaEmbeddings(model="qwen3-embedding:latest")

# 创建向量存储
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(all_splits)

# 构建用户查询
question = "黑悟空有哪些游戏场景?"

# 在向量存储中搜索相关内容,并准备上下文内容
retrieved_docs = vector_store.similarity_search(question, k=3)
docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

# 构建提示模板
prompt = ChatPromptTemplate.from_template("""
    基于以下上下文，回答问题。如果上下文中没有相关信息，
                请说"我无法从提供的上下文中找到相关信息"。
                上下文: {context}
                问题: {question}
                回答:
    """)

llm = ChatOllama(model=os.getenv("OLLAMA_MODEL"))
message = llm.invoke(prompt.format(context=docs_content, question=question))
print(message.content)
