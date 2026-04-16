<<<<<<< HEAD
<<<<<<< HEAD
import faiss
import numpy as np
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"
INDEX_DIR = BASE_DIR / "data" / "indexes"

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings.npy"
FAISS_FILE = INDEX_DIR / "faiss_index.bin"

# LOAD DATA
df = pd.read_parquet(PARQUET_FILE)
embeddings = np.load(EMBEDDING_FILE).astype("float32")

# BUILD INDEX IF NEEDED
if not FAISS_FILE.exists():
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, str(FAISS_FILE))
else:
    index = faiss.read_index(str(FAISS_FILE))

# QUERY
model = SentenceTransformer("all-MiniLM-L6-v2")

question = input("Semantic query: ")

query_vector = model.encode([question]).astype("float32")

distances, indices = index.search(query_vector, 5)

# RESULTS
results = df.iloc[indices[0]]

print(results[[
    "patient_id",
    "diagnoses",
    "labs",
    "medications"
]])
=======
=======
>>>>>>> app-v2
import faiss
import numpy as np
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"
INDEX_DIR = BASE_DIR / "data" / "indexes"

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings.npy"
FAISS_FILE = INDEX_DIR / "faiss_index.bin"

# LOAD DATA
df = pd.read_parquet(PARQUET_FILE)
embeddings = np.load(EMBEDDING_FILE).astype("float32")

# BUILD INDEX IF NEEDED
if not FAISS_FILE.exists():
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, str(FAISS_FILE))
else:
    index = faiss.read_index(str(FAISS_FILE))

# QUERY
model = SentenceTransformer("all-MiniLM-L6-v2")

question = input("Semantic query: ")

query_vector = model.encode([question]).astype("float32")

distances, indices = index.search(query_vector, 5)

# RESULTS
results = df.iloc[indices[0]]

print(results[[
    "patient_id",
    "diagnoses",
    "labs",
    "medications"
<<<<<<< HEAD
]])
>>>>>>> d3190ad (Add hybrid retrieval v2 prototype)
=======
]])
>>>>>>> app-v2
