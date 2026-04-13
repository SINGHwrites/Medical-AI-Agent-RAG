SELECT
    patient_id,
    STRING_AGG(DISTINCT test_name, ', ') AS labs
FROM read_csv_auto('data/raw/merged_patient_data.csv')
WHERE is_abnormal = 1
GROUP BY patient_id
LIMIT 20;