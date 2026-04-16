<<<<<<< HEAD
<<<<<<< HEAD
SELECT
    patient_id,
    STRING_AGG(DISTINCT test_name, ', ') AS labs
FROM read_csv_auto('data/raw/merged_patient_data.csv')
WHERE is_abnormal = 1
GROUP BY patient_id
=======
=======
>>>>>>> app-v2
SELECT
    patient_id,
    STRING_AGG(DISTINCT test_name, ', ') AS labs
FROM read_csv_auto('data/raw/merged_patient_data.csv')
WHERE is_abnormal = 1
GROUP BY patient_id
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
LIMIT 20;