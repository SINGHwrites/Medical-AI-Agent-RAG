<<<<<<< HEAD
<<<<<<< HEAD
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%type2_diabetes%'
=======
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%type2_diabetes%'
>>>>>>> aab3ca2 (Initial project import)
=======
SELECT *
FROM read_parquet('data/summaries/patient_summary.parquet')
WHERE diagnoses LIKE '%type2_diabetes%'
>>>>>>> app-v2
LIMIT 20;