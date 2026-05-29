from sentence_transformers import SentenceTransformer

class EmbeddingModel:

    def __init__(self, model_name = "all-MiniLM-L6-v2" ):
        self.model = SentenceTransformer(model_name)
        print("[Embedding model initialized]")

    def embed_documents(self, chunks):
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.model.encode(texts)
        return embeddings
    
    def embed_query(self, query):
        embedding = self.model.encode(query)
        return embedding

