SELECT
    patient_id,
    STRING_AGG(DISTINCT primary_diagnosis, ', ') AS diagnoses
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
LIMIT 20;