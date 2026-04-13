SELECT
    COUNT(*) - COUNT(age) AS age_nulls,
    COUNT(*) - COUNT(primary_diagnosis) AS diagnosis_nulls,
    COUNT(*) - COUNT(test_name) AS lab_nulls,
    COUNT(*) - COUNT(medication) AS medication_nulls
FROM read_csv_auto('data/raw/merged_patient_data.csv');