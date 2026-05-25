
from chat import RAGChatbot


chatbot = RAGChatbot()

while True:

    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == 'exit':
        break

    answer, results = chatbot.ask(query)

    print("\n---- Answer ---- \n")
    print(answer)

    print("\n--- Sources ---\n")

    metadatas = results["metadatas"][0]

    for metadata in metadatas:

        print(
            f"{metadata['source']} | Page {metadata['page']}"
        )