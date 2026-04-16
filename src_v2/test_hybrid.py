<<<<<<< HEAD
<<<<<<< HEAD
from retrieval.hybrid_retriever import hybrid_retrieve

question = input("Hybrid query: ")

df = hybrid_retrieve(question)

print(df[[
    "patient_id",
    "diagnoses",
    "labs",
    "medications"
]])
=======
=======
>>>>>>> app-v2
from retrieval.hybrid_retriever import hybrid_retrieve

question = input("Hybrid query: ")

df = hybrid_retrieve(question)

print(df[[
    "patient_id",
    "diagnoses",
    "labs",
    "medications"
<<<<<<< HEAD
]])
>>>>>>> d3190ad (Add hybrid retrieval v2 prototype)
=======
]])
>>>>>>> app-v2
