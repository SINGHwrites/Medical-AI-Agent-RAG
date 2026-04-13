<<<<<<< HEAD
from src_v2.retrieval.hybrid_retriever import hybrid_retrieve
from src_v2.summarizer.summary_builder import build_summary
from src_v2.llm.llm_rewriter import rewrite_summary

# QUESTION
question = input("Ask medical query: ")

# HYBRID RETRIEVAL
df = hybrid_retrieve(question)

# EMPTY RESULT CHECK
if df.empty:
    print("No matching patients found.")
    exit()

# STRUCTURED SUMMARY
summary = build_summary(df)

# STRUCTURED ANSWER
print("\n--- STRUCTURED ANSWER ---")
print(f"Patients found: {summary['count']}")
print(f"Age range: {summary['age_min']} to {summary['age_max']}")

print("\nTop diagnoses:")
for item in summary["diagnoses"]:
    print(f"- {item}")

print("\nTop labs:")
for item in summary["labs"]:
    print(f"- {item}")

print("\nTop medications:")
for item in summary["medications"]:
    print(f"- {item}")

# OPTIONAL LLM ANSWER
print("\n--- LLM ANSWER ---")
print(rewrite_summary(summary))
=======
from pathlib import Path
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from src_v2.llm.llm_rewriter import rewrite_summary
    from src_v2.retrieval.retriever import retrieve_patients
    from src_v2.summarizer.summary_builder import build_summary
else:
    from ..llm.llm_rewriter import rewrite_summary
    from ..retrieval.retriever import retrieve_patients
    from ..summarizer.summary_builder import build_summary


def main() -> int:
    question = input("Ask medical query: ").strip()

    if not question:
        print("Please enter a medical query.")
        return 1

    df = retrieve_patients(question)

    if df.empty:
        print("No matching patients found.")
        return 0

    summary = build_summary(df)

    print("\n--- STRUCTURED ANSWER ---")
    print(summary)

    print("\n--- LLM ANSWER ---")
    print(rewrite_summary(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
>>>>>>> aab3ca2 (Initial project import)
