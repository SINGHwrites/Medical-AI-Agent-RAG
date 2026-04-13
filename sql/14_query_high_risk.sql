SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE age > 70
AND diagnoses LIKE '%type2_diabetes%'
AND labs LIKE '%creatinine%'
LIMIT 20;