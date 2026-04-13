SELECT
    patient_id,
    MIN(age) AS age,
    MIN(sex) AS sex,
    MIN(bmi) AS bmi,
    MIN(smoking_status) AS smoking_status,
    MIN(alcohol_use) AS alcohol_use,
    MIN(exercise_level) AS exercise_level
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
LIMIT 20;