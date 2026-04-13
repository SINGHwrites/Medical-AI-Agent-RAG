<<<<<<< HEAD
SELECT
    patient_id,
    STRING_AGG(DISTINCT medication, ', ') AS medications
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
=======
SELECT
    patient_id,
    STRING_AGG(DISTINCT medication, ', ') AS medications
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
>>>>>>> aab3ca2 (Initial project import)
LIMIT 20;