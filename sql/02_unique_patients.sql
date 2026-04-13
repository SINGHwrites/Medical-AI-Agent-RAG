SELECT COUNT(DISTINCT patient_id) AS unique_patients
FROM read_csv_auto('data/raw/merged_patient_data.csv');