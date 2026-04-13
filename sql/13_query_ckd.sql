<<<<<<< HEAD
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%chronic_kidney_disease%'
=======
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%chronic_kidney_disease%'
>>>>>>> aab3ca2 (Initial project import)
LIMIT 20;