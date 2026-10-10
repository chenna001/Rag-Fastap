# import faiss


# def create_vector_index(dimension: int = 3072):

#     index = faiss.IndexFlatL2(dimension)

#     return index

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ new code add
# import faiss
# import numpy as np


# def create_vector_index(embeddings: list[list[float]]):

#     vectors = np.array(embeddings, dtype="float32")

#     dimension = vectors.shape[1]

#     print("Vector shape:", vectors.shape)
#     print("Vector dimension:", dimension)

#     index = faiss.IndexFlatL2(dimension)

#     index.add(vectors)

#     return index

#update another code 

import faiss
import numpy as np

# Keep the index and chunks available while the app is running.
index = None
stored_chunks = []


def add_chunks_to_index(
    chunks: list[str],
    embeddings: list[list[float]]
):
    global index, stored_chunks

    vectors = np.asarray(embeddings, dtype="float32")

    if vectors.ndim != 2 or len(vectors) != len(chunks):
        raise ValueError("Chunks and embeddings do not match")

    if len(vectors) == 0:
        raise ValueError("No embeddings provided")

    if index is None:
        index = faiss.IndexFlatL2(vectors.shape[1])

    if vectors.shape[1] != index.d:
        raise ValueError("Embedding dimensions do not match the index")

    index.add(vectors)
    stored_chunks.extend(chunks)

    print("Total vectors:", index.ntotal)
    print("Vector dimension:", index.d)


def search_chunks(
    query_embedding: list[float],
    top_k: int = 3
) -> list[str]:
    if index is None or index.ntotal == 0:
        raise ValueError("No documents have been uploaded")

    query_vector = np.asarray(
        [query_embedding],
        dtype="float32"
    )

    if query_vector.shape[1] != index.d:
        raise ValueError("Query embedding dimension mismatch")

    k = min(top_k, index.ntotal)
    distances, indices = index.search(query_vector, k)

    results = []

    for idx in indices[0]:
        if idx >= 0:
            results.append(stored_chunks[int(idx)])

    return results
