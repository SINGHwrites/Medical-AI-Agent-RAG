import pandas as pd

SOURCE = "data/summaries/patient_summary.parquet"
TARGET = "data/deploy/summaries/patient_summary_deploy.parquet"

df = pd.read_parquet(SOURCE)

df = df.head(5000)

df.to_parquet(TARGET)

print(df.shape)
print("Deploy parquet created.")