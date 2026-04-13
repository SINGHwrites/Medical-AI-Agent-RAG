<<<<<<< HEAD
import duckdb
import pandas as pd
from pathlib import Path
from transformers import pipeline

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent
PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"

# CONNECT DB
con = duckdb.connect()

# LOAD MODEL
print("Loading model...")

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200
)

# USER QUESTION
question = input("Ask medical query: ").lower()

# CONDITIONS
conditions = []

if "elderly" in question or "old" in question:
    conditions.append("age > 70")

if "diabetes" in question:
    conditions.append("diagnoses LIKE '%type2_diabetes%'")

if "kidney" in question or "creatinine" in question:
    conditions.append("labs LIKE '%creatinine%'")

if "hypertension" in question:
    conditions.append("diagnoses LIKE '%hypertension%'")

if "obesity" in question:
    conditions.append("diagnoses LIKE '%obesity%'")

if "readmitted" in question:
    conditions.append("readmitted_30d = 1")

# SQL
query = f"""
SELECT *
FROM read_parquet('{str(PARQUET_FILE).replace("\\", "/")}')
"""

if conditions:
    query += "\nWHERE " + " AND ".join(conditions)

query += "\nLIMIT 100"

df = con.execute(query).fetchdf()

# SUMMARY
count = len(df)

age_min = df["age"].min()
age_max = df["age"].max()

diagnosis_text = ",".join(df["diagnoses"].dropna().astype(str))
top_diagnoses = pd.Series(diagnosis_text.split(",")).str.strip().value_counts().head(5)

lab_text = ",".join(df["labs"].dropna().astype(str))
top_labs = pd.Series(lab_text.split(",")).str.strip().value_counts().head(5)

med_text = ",".join(df["medications"].dropna().astype(str))
top_meds = pd.Series(med_text.split(",")).str.strip().value_counts().head(5)

# PROMPT
prompt = f"""
Rewrite this medical summary in one sentence without adding facts:

Patients found: {count}
Age range: {age_min}-{age_max}
Diagnoses: {', '.join(top_diagnoses.index)}
Labs: {', '.join(top_labs.index)}
Medications: {', '.join(top_meds.index)}

Sentence:
"""

# LLM OUTPUT
output = generator(prompt)[0]["generated_text"]

answer = output.split("Sentence:")[-1].strip()
answer = answer.split("\n")[0]

print("\n--- LLM ANSWER ---")
print(answer)

#diabetes kidney elderly
#obesity icu
=======
import duckdb
import pandas as pd
from pathlib import Path
from transformers import pipeline

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent
PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"

# CONNECT DB
con = duckdb.connect()

# LOAD MODEL
print("Loading model...")

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200
)

# USER QUESTION
question = input("Ask medical query: ").lower()

# CONDITIONS
conditions = []

if "elderly" in question or "old" in question:
    conditions.append("age > 70")

if "diabetes" in question:
    conditions.append("diagnoses LIKE '%type2_diabetes%'")

if "kidney" in question or "creatinine" in question:
    conditions.append("labs LIKE '%creatinine%'")

if "hypertension" in question:
    conditions.append("diagnoses LIKE '%hypertension%'")

if "obesity" in question:
    conditions.append("diagnoses LIKE '%obesity%'")

if "readmitted" in question:
    conditions.append("readmitted_30d = 1")

# SQL
query = f"""
SELECT *
FROM read_parquet('{str(PARQUET_FILE).replace("\\", "/")}')
"""

if conditions:
    query += "\nWHERE " + " AND ".join(conditions)

query += "\nLIMIT 100"

df = con.execute(query).fetchdf()

# SUMMARY
count = len(df)

age_min = df["age"].min()
age_max = df["age"].max()

diagnosis_text = ",".join(df["diagnoses"].dropna().astype(str))
top_diagnoses = pd.Series(diagnosis_text.split(",")).str.strip().value_counts().head(5)

lab_text = ",".join(df["labs"].dropna().astype(str))
top_labs = pd.Series(lab_text.split(",")).str.strip().value_counts().head(5)

med_text = ",".join(df["medications"].dropna().astype(str))
top_meds = pd.Series(med_text.split(",")).str.strip().value_counts().head(5)

# PROMPT
prompt = f"""
Rewrite this medical summary in one sentence without adding facts:

Patients found: {count}
Age range: {age_min}-{age_max}
Diagnoses: {', '.join(top_diagnoses.index)}
Labs: {', '.join(top_labs.index)}
Medications: {', '.join(top_meds.index)}

Sentence:
"""

# LLM OUTPUT
output = generator(prompt)[0]["generated_text"]

answer = output.split("Sentence:")[-1].strip()
answer = answer.split("\n")[0]

print("\n--- LLM ANSWER ---")
print(answer)

#diabetes kidney elderly
#obesity icu
>>>>>>> aab3ca2 (Initial project import)
#hypertension death