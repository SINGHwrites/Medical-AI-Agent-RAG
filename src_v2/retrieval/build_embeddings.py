<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"
INDEX_DIR = BASE_DIR / "data" / "indexes"

INDEX_DIR.mkdir(exist_ok=True)

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings.npy"

# LOAD DATA
df = pd.read_parquet(PARQUET_FILE)

# BUILD TEXT FOR EMBEDDING
texts = (
    "Age " + df["age"].astype(str) +
    " Sex " + df["sex"].astype(str) +
    " Diagnoses " + df["diagnoses"].fillna("") +
    " Labs " + df["labs"].fillna("") +
    " Medications " + df["medications"].fillna("")
).tolist()

# MODEL
model = SentenceTransformer("all-MiniLM-L6-v2")

# EMBEDDINGS
embeddings = model.encode(
    texts,
    show_progress_bar=True,
    batch_size=256
)

# SAVE
np.save(EMBEDDING_FILE, embeddings)

print("Embeddings saved.")
print(embeddings.shape)
=======
=======
>>>>>>> app-v2
import pandas as pd
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"
INDEX_DIR = BASE_DIR / "data" / "indexes"

INDEX_DIR.mkdir(exist_ok=True)

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings.npy"

# LOAD DATA
df = pd.read_parquet(PARQUET_FILE)

# BUILD TEXT FOR EMBEDDING
texts = (
    "Age " + df["age"].astype(str) +
    " Sex " + df["sex"].astype(str) +
    " Diagnoses " + df["diagnoses"].fillna("") +
    " Labs " + df["labs"].fillna("") +
    " Medications " + df["medications"].fillna("")
).tolist()

# MODEL
model = SentenceTransformer("all-MiniLM-L6-v2")

# EMBEDDINGS
embeddings = model.encode(
    texts,
    show_progress_bar=True,
    batch_size=256
)

# SAVE
np.save(EMBEDDING_FILE, embeddings)

print("Embeddings saved.")
<<<<<<< HEAD
print(embeddings.shape)
>>>>>>> d3190ad (Add hybrid retrieval v2 prototype)
=======
print(embeddings.shape)
>>>>>>> app-v2
