import numpy as np
import faiss

SOURCE = "data/deploy/faiss/patient_embeddings_deploy.npy"
TARGET = "data/deploy/faiss/patient_index_deploy.faiss"

embeddings = np.load(SOURCE).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, TARGET)

print(index.ntotal)
print("Deploy FAISS index created.")