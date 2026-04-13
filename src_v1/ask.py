import duckdb
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

# age intent
if "elderly" in question or "old" in question:
    conditions.append("age > 70")

# diabetes intent
if "diabetes" in question:
    conditions.append("diagnoses LIKE '%type2_diabetes%'")

# kidney intent
if "kidney" in question or "creatinine" in question:
    conditions.append("labs LIKE '%creatinine%'")

# hypertension intent
if "hypertension" in question:
    conditions.append("diagnoses LIKE '%hypertension%'")

# obesity intent
if "obesity" in question:
    conditions.append("diagnoses LIKE '%obesity%'")

# readmission intent
if "readmitted" in question:
    conditions.append("readmitted_30d = 1")

# ICU intent
if "icu" in question:
    conditions.append("icu_admission = 1")

# death intent
if "death" in question:
    conditions.append("in_hospital_death = 1")

# DEFAULT QUERY
query = f"""
SELECT *
FROM read_parquet('{str(PARQUET_FILE).replace("\\", "/")}')
"""

# APPLY CONDITIONS
if conditions:
    query += "\nWHERE " + " AND ".join(conditions)
query += "\nLIMIT 20"

# RUN QUERY
print("\nGenerated SQL:")
print(query)

result = con.execute(query).fetchdf()

print("\nResults:")
print(result)