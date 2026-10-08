# import faiss


# def create_vector_index(dimension: int = 3072):

#     index = faiss.IndexFlatL2(dimension)

#     return index

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ new code add
import faiss
import numpy as np


def create_vector_index(embeddings: list[list[float]]):

    vectors = np.array(embeddings, dtype="float32")

    dimension = vectors.shape[1]

    print("Vector shape:", vectors.shape)
    print("Vector dimension:", dimension)

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index