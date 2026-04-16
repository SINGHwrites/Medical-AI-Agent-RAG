<<<<<<< HEAD
<<<<<<< HEAD
SELECT COUNT(DISTINCT patient_id) AS unique_patients
=======
SELECT COUNT(DISTINCT patient_id) AS unique_patients
>>>>>>> aab3ca2 (Initial project import)
=======
SELECT COUNT(DISTINCT patient_id) AS unique_patients
>>>>>>> app-v2
FROM read_csv_auto('data/raw/merged_patient_data.csv');