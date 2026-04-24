from src_v2.retrieval.hybrid_retriever import hybrid_retrieve
from src_v2.summarizer.summary_builder import build_summary

def main() -> int:
    question = input("Ask medical query: ").strip()
    if not question:
        print("Please enter a medical query.")
        return 1

    df = hybrid_retrieve(question)

    if df.empty:
        print("No matching patients found.")
        return 0

    summary = build_summary(df)

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

    print("\n--- LLM ANSWER ---")
    try:
        from src_v2.llm.llm_rewriter import rewrite_summary
        print(rewrite_summary(summary))
    except Exception as exc:
        print(f"LLM unavailable: {exc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
