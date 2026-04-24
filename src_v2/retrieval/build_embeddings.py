import pandas as pd
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARQUET_FILE = BASE_DIR / "data" / "deploy" / "summaries" / "patient_summary_deploy.parquet"
INDEX_DIR = BASE_DIR / "data" / "deploy" / "faiss"

INDEX_DIR.mkdir(parents=True, exist_ok=True)

EMBEDDING_FILE = INDEX_DIR / "patient_embeddings_deploy.npy"


def main() -> int:
    df = pd.read_parquet(PARQUET_FILE)

    texts = (
        "Age " + df["age"].astype(str) +
        " Sex " + df["sex"].astype(str) +
        " Diagnoses " + df["diagnoses"].fillna("") +
        " Labs " + df["labs"].fillna("") +
        " Medications " + df["medications"].fillna("")
    ).tolist()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=256
    )

    np.save(EMBEDDING_FILE, embeddings)

    print("Embeddings saved.")
    print(embeddings.shape)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
