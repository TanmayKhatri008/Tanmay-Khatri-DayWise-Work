import chromadb

class VectorDB:

    def __init__(self, collection_name = "rag_collection"):

        self.client = chromadb.PersistentClient(path="../db")
        self.collection=  self.client.get_or_create_collection(name = collection_name)
        print("vector db instance initialized")

    def add_documents(self, chunks, embeddings):
        documents = [chunk["text"] for chunk in chunks]

        metadatas = [{
            "source": chunk["source"],
            "page": chunk["page"]
        } for chunk in chunks]

        ids = [str(i) for i in range(len(chunks))]

        self.collection.add(
            documents = documents,
            embeddings = embeddings.tolist(),
            metadatas = metadatas,
            ids = ids
        )


    def similarity_search(self, query_embedding, top_k = 8):

        results = self.collection.query(
            query_embeddings = [query_embedding.tolist()],
            n_results = top_k
        )

        return results



if __name__ == "__main__":

    from pdf_loader import load_all_pdfs
    from chunking import chunk_text
    from embeddings import EmbeddingModel

    documents = load_all_pdfs("../data")

    chunks = chunk_text(documents)

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.embed_documents(chunks)

    vectordb = VectorDB("nlp")

    vectordb.add_documents(chunks, embeddings)

    query = "What is retrieval augmented generation?"

    query_embedding = embedding_model.embed_query(query)

    results = vectordb.similarity_search(query_embedding)

    print("\n--- Search Results ---\n")

    retrieved_docs = results["documents"][0]
    retrieved_metadata = results["metadatas"][0]

    for i in range(len(retrieved_docs)):

        print(f"\nResult {i+1}")
        print(f"Source: {retrieved_metadata[i]['source']}")
        print(f"Page: {retrieved_metadata[i]['page']}")

        print("\nText:\n")

        print(retrieved_docs[i][:500])