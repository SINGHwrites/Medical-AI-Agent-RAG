<<<<<<< HEAD
SELECT primary_diagnosis, COUNT(*) AS freq
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY primary_diagnosis
ORDER BY freq DESC
=======
SELECT primary_diagnosis, COUNT(*) AS freq
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY primary_diagnosis
ORDER BY freq DESC
>>>>>>> aab3ca2 (Initial project import)
LIMIT 20;