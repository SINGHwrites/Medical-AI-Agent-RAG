SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%chronic_kidney_disease%'
LIMIT 20;