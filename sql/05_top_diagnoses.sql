SELECT primary_diagnosis, COUNT(*) AS freq
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY primary_diagnosis
ORDER BY freq DESC
LIMIT 20;