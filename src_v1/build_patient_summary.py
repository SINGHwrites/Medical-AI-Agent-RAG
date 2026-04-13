import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "raw" / "merged_patient_data.csv"
SQL_FILE = BASE_DIR / "sql" / "11_patient_summary.sql"
OUTPUT_FILE = BASE_DIR / "outputs" / "11_patient_summary_sample.csv"

con = duckdb.connect()

with open(SQL_FILE, "r", encoding="utf-8") as f:
    query = f.read()

query = query.replace("data/raw/merged_patient_data.csv", str(DATA_FILE).replace("\\", "/"))

result = con.execute(query).fetchdf()

result.to_csv(OUTPUT_FILE, index=False)

print(result.head())
print(f"Saved: {OUTPUT_FILE}")
