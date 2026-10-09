import bs4
from langchain_community.document_loaders import WebBaseLoader

page_url = "https://zh.wikipedia.org/wiki/黑神话：悟空"

loader = WebBaseLoader(web_paths=[page_url], bs_kwargs={"parse_only": bs4.SoupStrainer(id="bodyContent")})
docs = []
docs = loader.load()
assert len(docs) == 1
doc = docs[0]

print(f"{doc.metadata}\n")
print(doc.page_content)


