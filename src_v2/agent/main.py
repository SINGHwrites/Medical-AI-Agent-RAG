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