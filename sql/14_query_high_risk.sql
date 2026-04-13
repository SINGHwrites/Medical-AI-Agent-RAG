<<<<<<< HEAD
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE age > 70
AND diagnoses LIKE '%type2_diabetes%'
AND labs LIKE '%creatinine%'
=======
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE age > 70
AND diagnoses LIKE '%type2_diabetes%'
AND labs LIKE '%creatinine%'
>>>>>>> aab3ca2 (Initial project import)
LIMIT 20;