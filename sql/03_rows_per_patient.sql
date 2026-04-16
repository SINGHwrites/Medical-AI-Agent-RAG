<<<<<<< HEAD
<<<<<<< HEAD
SELECT AVG(cnt) AS avg_rows_per_patient
FROM (
    SELECT patient_id, COUNT(*) AS cnt
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
=======
=======
>>>>>>> app-v2
SELECT AVG(cnt) AS avg_rows_per_patient
FROM (
    SELECT patient_id, COUNT(*) AS cnt
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
);