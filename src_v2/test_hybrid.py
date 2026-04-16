from retrieval.hybrid_retriever import hybrid_retrieve

question = input("Hybrid query: ")

df = hybrid_retrieve(question)

print(df[[
    "patient_id",
    "diagnoses",
    "labs",
    "medications"
]])
