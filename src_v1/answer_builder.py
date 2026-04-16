import duckdb
import pandas as pd
from pathlib import Path

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent
PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"

# CONNECT
con = duckdb.connect()

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

if "icu" in question:
    conditions.append("icu_admission = 1")

if "death" in question:
    conditions.append("in_hospital_death = 1")

# SQL QUERY
query = f"""
SELECT *
FROM read_parquet('{str(PARQUET_FILE).replace("\\", "/")}')
"""

if conditions:
    query += "\nWHERE " + " AND ".join(conditions)

query += "\nLIMIT 100"

# RUN QUERY
df = con.execute(query).fetchdf()

# NO RESULTS
if df.empty:
    print("\nNo matching patients found.")
    exit()

# SUMMARY METRICS
count = len(df)

age_min = df["age"].min()
age_max = df["age"].max()

# diagnoses
diagnosis_text = ",".join(df["diagnoses"].dropna().astype(str))
top_diagnoses = pd.Series(diagnosis_text.split(",")).str.strip().value_counts().head(5)

# labs
lab_text = ",".join(df["labs"].dropna().astype(str))
top_labs = pd.Series(lab_text.split(",")).str.strip().value_counts().head(5)

# medications
med_text = ",".join(df["medications"].dropna().astype(str))
top_meds = pd.Series(med_text.split(",")).str.strip().value_counts().head(5)

# ANSWER
print("\n--- MEDICAL ANSWER ---")

print(f"\n{count} matching patients found.")
print(f"Age range: {age_min} to {age_max}")

print("\nTop diagnoses:")
for item in top_diagnoses.index:
    print(f"- {item}")

print("\nTop abnormal labs:")
for item in top_labs.index:
    print(f"- {item}")

print("\nTop medications:")
for item in top_meds.index:
    print(f"- {item}")