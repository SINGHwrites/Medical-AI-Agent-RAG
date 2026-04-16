<<<<<<< HEAD
<<<<<<< HEAD
SELECT
    patient_id,
    STRING_AGG(DISTINCT primary_diagnosis, ', ') AS diagnoses
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
=======
=======
>>>>>>> app-v2
SELECT
    patient_id,
    STRING_AGG(DISTINCT primary_diagnosis, ', ') AS diagnoses
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
LIMIT 20;