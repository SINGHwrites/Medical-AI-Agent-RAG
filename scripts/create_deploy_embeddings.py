import numpy as np

SOURCE = "data/indexes/patient_embeddings.npy"
TARGET = "data/deploy/faiss/patient_embeddings_deploy.npy"

embeddings = np.load(SOURCE)

deploy_embeddings = embeddings[:5000]

np.save(TARGET, deploy_embeddings)

print(deploy_embeddings.shape)
print("Deploy embeddings created.")