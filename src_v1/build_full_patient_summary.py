<<<<<<< HEAD
<<<<<<< HEAD
import duckdb
from pathlib import Path

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "raw" / "merged_patient_data.csv"
SQL_FILE = BASE_DIR / "sql" / "11_patient_summary.sql"

CSV_OUT = BASE_DIR / "data" / "summaries" / "patient_summary.csv"
PARQUET_OUT = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"

# CONNECT
con = duckdb.connect()

# LOAD SQL
with open(SQL_FILE, "r", encoding="utf-8") as f:
    query = f.read()
query = query.replace(
    "data/raw/merged_patient_data.csv",
    str(DATA_FILE).replace("\\", "/")
)

# EXECUTE
print("Building full patient summary...")
result = con.execute(query).fetchdf()

# SAVE CSV
result.to_csv(CSV_OUT, index=False)

# SAVE PARQUET
result.to_parquet(PARQUET_OUT, index=False)

# VERIFY
print(result.shape)
print(result.head())

print(f"Saved CSV: {CSV_OUT}")
print(f"Saved Parquet: {PARQUET_OUT}")
=======
=======
>>>>>>> app-v2
import duckdb
from pathlib import Path

# PATHS
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "raw" / "merged_patient_data.csv"
SQL_FILE = BASE_DIR / "sql" / "11_patient_summary.sql"

CSV_OUT = BASE_DIR / "data" / "summaries" / "patient_summary.csv"
PARQUET_OUT = BASE_DIR / "data" / "summaries" / "patient_summary.parquet"

# CONNECT
con = duckdb.connect()

# LOAD SQL
with open(SQL_FILE, "r", encoding="utf-8") as f:
    query = f.read()
query = query.replace(
    "data/raw/merged_patient_data.csv",
    str(DATA_FILE).replace("\\", "/")
)

# EXECUTE
print("Building full patient summary...")
result = con.execute(query).fetchdf()

# SAVE CSV
result.to_csv(CSV_OUT, index=False)

# SAVE PARQUET
result.to_parquet(PARQUET_OUT, index=False)

# VERIFY
print(result.shape)
print(result.head())

print(f"Saved CSV: {CSV_OUT}")
print(f"Saved Parquet: {PARQUET_OUT}")
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
