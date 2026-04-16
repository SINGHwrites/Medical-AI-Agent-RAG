SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%type2_diabetes%'
LIMIT 20;