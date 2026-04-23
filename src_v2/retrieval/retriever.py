import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PARQUET_FILE = BASE_DIR / "data" / "deploy" / "summaries" / "patient_summary_deploy.parquet"

def retrieve_patients(question: str):
    con = duckdb.connect()
    
    con.execute("PRAGMA threads=6")

    question = question.lower()
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

    parquet_path = str(PARQUET_FILE).replace("\\", "/")

    query = f"""
    SELECT *
    FROM read_parquet('{parquet_path}')
    """

    if conditions:
        query += "\nWHERE " + " AND ".join(conditions)

    #query += "\nLIMIT 100000"
    return con.execute(query).fetchdf()