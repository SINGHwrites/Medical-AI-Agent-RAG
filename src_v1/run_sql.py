import duckdb
from pathlib import Path

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "raw" / "merged_patient_data.csv"
SQL_DIR = BASE_DIR / "sql"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# CONNECT DUCKDB
con = duckdb.connect()

# SQL FILES TO RUN
sql_files = [
    "01_row_count.sql",
    "02_unique_patients.sql",
    "03_rows_per_patient.sql",
    "04_null_profile.sql",
    "05_top_diagnoses.sql",
    "06_patient_demographics.sql",
    "07_patient_diagnoses.sql",
    "08_patient_labs.sql",
    "09_patient_medications.sql",
    "10_patient_outcomes.sql"
]

# EXECUTE EACH QUERY
for file_name in sql_files:
    sql_path = SQL_DIR / file_name

    with open(sql_path, "r", encoding="utf-8") as f:
        query = f.read()
        
    # replace file path placeholder if needed
    query = query.replace("data/raw/merged_patient_data.csv", str(DATA_FILE).replace("\\", "/"))
    
    print(f"\nRunning: {file_name}")
    
    result = con.execute(query).fetchdf()
    print(result)

    # save output
    out_file = OUTPUT_DIR / f"{file_name.replace('.sql', '.csv')}"
    result.to_csv(out_file, index=False)
    print(f"Saved: {out_file}")