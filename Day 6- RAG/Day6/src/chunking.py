def chunk_text(documents, chunk_size = 1000, overlap = 500):
    chunks = []

    for doc in documents:
        text = doc["text"]
        start = 0
        while start<len(text):
            end = start+chunk_size
            chunk = text[start:end]     
            chunks.append({
                "source": doc["source"],
                "page": doc["page"],
                "text": chunk
            })

            start+= chunk_size - overlap

    return chunks



