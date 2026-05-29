from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

print("Loading PDF...")

loader = PyPDFLoader("document loaders/AI_Unit_1.pdf")
documents = loader.load()
print("Splitting document into chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

embedding_model = HuggingFaceEmbeddings()

print("Creating vector database...")

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

print("Database created successfully")