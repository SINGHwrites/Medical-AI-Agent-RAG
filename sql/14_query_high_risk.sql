<<<<<<< HEAD
<<<<<<< HEAD
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE age > 70
AND diagnoses LIKE '%type2_diabetes%'
AND labs LIKE '%creatinine%'
=======
=======
>>>>>>> app-v2
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE age > 70
AND diagnoses LIKE '%type2_diabetes%'
AND labs LIKE '%creatinine%'
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
LIMIT 20;