import faiss
import numpy as np
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer
from src_v2.retrieval.retriever import retrieve_patients

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"
INDEX_DIR = BASE_DIR / "data" / "indexes"

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings.npy"
FAISS_FILE = INDEX_DIR / "faiss_index.bin"

# LOAD STATIC OBJECTS ONCE
df_all = pd.read_parquet(PARQUET_FILE)

embeddings = np.load(EMBEDDING_FILE).astype("float32")

index = faiss.read_index(str(FAISS_FILE))

model = SentenceTransformer("all-MiniLM-L6-v2")

# HYBRID RETRIEVAL
def hybrid_retrieve(question: str):

    # SQL RETRIEVAL
    sql_df = retrieve_patients(question)

    # VECTOR RETRIEVAL
    query_vector = model.encode([question]).astype("float32")

    distances, indices = index.search(query_vector, 5)

    vector_df = df_all.iloc[indices[0]]

    # MERGE
    merged = pd.concat([sql_df, vector_df])

    merged = merged.drop_duplicates(subset=["patient_id"])

    # LIMIT FINAL SIZE
    merged = merged.head(100)

    return merged