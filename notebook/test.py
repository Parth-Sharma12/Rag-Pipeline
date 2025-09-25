import chromadb, uuid

client = chromadb.Client()
col = client.get_or_create_collection("test")

ids = [str(uuid.uuid4()) for _ in range(2)]
docs = ["Doc one content", "Doc two content"]
embs = [[0.1]*384, [0.2]*384]  # fake embeddings
metas = [{"doc_index":0}, {"doc_index":1}]

col.add(ids=ids, documents=docs, embeddings=embs, metadatas=metas)
print("Inserted 2 docs.")
