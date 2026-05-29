from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
embedding_model = HuggingFaceEmbeddings()

vector_store = Chroma(
  persist_directory="chroma-db",
  embedding_function=embedding_model
  )
retriever = vector_store.as_retriever(
  search_type="similarity",
  search_kwargs={"k": 4}
  )

llm = ChatMistralAI(model="mistral-small-2506")
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
        You are a document assistant.
        Answer only using the provided context.
        If the answer is not available in the context,
        respond with:
        "Couldn't find such information in the document."
        Do not create your own information.
        """,
        ),
        (
            "human",
            """
        Context:
        {context}

        Question:
        {question}
        """,
        ),
    ]
)

print("=" * 50)
print("RAG Chat System Started")
print("Type 0 to exit")
print("=" * 50)

while True:
    user_query = input("\nYou: ")
    if user_query == "0":
        print("Exiting...")
        break

    docs = retriever.invoke(user_query)
    if not docs:
        print("\nAI: Couldn't find such information in the document.")
        continue

    context = "\n\n".join(doc.page_content for doc in docs)
    final_prompt = prompt.invoke({"context": context, "question": user_query})
    response = llm.invoke(final_prompt)
    print(f"\nAI: {response.content}")
    
