import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PARQUET_FILE = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"
SQL_DIR = BASE_DIR / "sql"

con = duckdb.connect()

sql_files = [
    "12_query_diabetes.sql",
    "13_query_ckd.sql",
    "14_query_high_risk.sql"
]

for file_name in sql_files:
    sql_path = SQL_DIR / file_name
    
    with open(sql_path, "r", encoding="utf-8") as f:
        query = f.read()
       
    query = query.replace(
        "data/summaries/patient_summary.parquet",
        str(PARQUET_FILE).replace("\\", "/")
    )
    
    print(f"\nRunning: {file_name}")

    result = con.execute(query).fetchdf()
    print(result.head())