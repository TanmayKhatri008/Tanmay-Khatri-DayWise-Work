import os
from groq import Groq
from dotenv import load_dotenv
from embeddings import EmbeddingModel
from vectordb import VectorDB

load_dotenv()

class RAGChatbot:

    def __init__(self):
        self.client = Groq(
            api_key = os.getenv("GROQ_API_KEY")
        )

        self.embedding_model = EmbeddingModel()
        self.vectordb = VectorDB("nlp")
        
        print("[INFO] chatbot object initialized")

    def build_context(self, results):

        documents = results["documents"][0]
        context = "\n\n".join(documents)
        return context
    
    def ask(self, query, top_k=3):
        query_embedding = self.embedding_model.embed_query(query)

        results = self.vectordb.similarity_search(
            query_embedding,
            top_k=top_k
        )

        context = self.build_context(results)

        prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find the answer in the provided documents."

Context:
{context}

Question:
{query}
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content
        return answer, results