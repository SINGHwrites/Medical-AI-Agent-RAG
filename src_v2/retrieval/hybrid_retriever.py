import faiss
faiss.omp_set_num_threads(4)
import numpy as np
import pandas as pd
from functools import lru_cache
from pathlib import Path
from sentence_transformers import SentenceTransformer
from src_v2.retrieval.retriever import retrieve_patients

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "deploy" / "summaries" / "patient_summary_deploy.parquet"

INDEX_DIR = BASE_DIR / "data" / "deploy" / "faiss"

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings_deploy.npy"
FAISS_FILE = INDEX_DIR / "patient_index_deploy.faiss"


@lru_cache(maxsize=1)
def _load_index_data():
    df_all = pd.read_parquet(PARQUET_FILE)
    if EMBEDDING_FILE.exists():
        np.load(EMBEDDING_FILE)
    index = faiss.read_index(str(FAISS_FILE))
    return df_all, index


@lru_cache(maxsize=1)
def _get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

# HYBRID RETRIEVAL
def hybrid_retrieve(question: str):
    if not question.strip():
        return pd.DataFrame()
    df_all, index = _load_index_data()
    model = _get_model()

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
