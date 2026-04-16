<<<<<<< HEAD
<<<<<<< HEAD
SELECT primary_diagnosis, COUNT(*) AS freq
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY primary_diagnosis
ORDER BY freq DESC
=======
=======
>>>>>>> app-v2
SELECT primary_diagnosis, COUNT(*) AS freq
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY primary_diagnosis
ORDER BY freq DESC
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
LIMIT 20;