import faiss
import numpy as np
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "deploy" / "summaries" / "patient_summary_deploy.parquet"
INDEX_DIR = BASE_DIR / "data" / "deploy" / "faiss"

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings_deploy.npy"
FAISS_FILE = INDEX_DIR / "patient_index_deploy.faiss"


def main() -> int:
    df = pd.read_parquet(PARQUET_FILE)
    embeddings = np.load(EMBEDDING_FILE).astype("float32")

    if not FAISS_FILE.exists():
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        faiss.write_index(index, str(FAISS_FILE))
    else:
        index = faiss.read_index(str(FAISS_FILE))

    model = SentenceTransformer("all-MiniLM-L6-v2")

    question = input("Semantic query: ").strip()
    if not question:
        print("Please enter a query.")
        return 1

    query_vector = model.encode([question]).astype("float32")
    distances, indices = index.search(query_vector, 5)
    results = df.iloc[indices[0]]

    print(results[[
        "patient_id",
        "diagnoses",
        "labs",
        "medications"
    ]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
