from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter=RecursiveCharacterTextSplitter(
  chunk_size=20,
  chunk_overlap=3
)

loader = TextLoader(r"E:\Gen AI\Day 7\document loaders\notes.txt")

docs = loader.load()

chunks=splitter.split_documents(docs)

for i in chunks:
  print(i.page_content)
  print()