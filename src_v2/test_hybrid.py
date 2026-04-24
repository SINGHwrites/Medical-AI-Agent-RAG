from src_v2.retrieval.hybrid_retriever import hybrid_retrieve


def main() -> int:
    question = input("Hybrid query: ").strip()
    if not question:
        print("Please enter a query.")
        return 1

    df = hybrid_retrieve(question)

    print(df[[
        "patient_id",
        "diagnoses",
        "labs",
        "medications"
    ]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
