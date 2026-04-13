<<<<<<< HEAD
SELECT
    patient_id,
    STRING_AGG(DISTINCT test_name, ', ') AS labs
FROM read_csv_auto('data/raw/merged_patient_data.csv')
WHERE is_abnormal = 1
GROUP BY patient_id
=======
SELECT
    patient_id,
    STRING_AGG(DISTINCT test_name, ', ') AS labs
FROM read_csv_auto('data/raw/merged_patient_data.csv')
WHERE is_abnormal = 1
GROUP BY patient_id
>>>>>>> aab3ca2 (Initial project import)
LIMIT 20;