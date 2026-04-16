<<<<<<< HEAD
<<<<<<< HEAD
WITH demographics AS (
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
),

diagnoses AS (
    SELECT
        patient_id,
        STRING_AGG(DISTINCT primary_diagnosis, ', ') AS diagnoses
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
),

labs AS (
    SELECT
        patient_id,
        STRING_AGG(DISTINCT test_name, ', ') AS labs
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    WHERE is_abnormal = 1
    GROUP BY patient_id
),

medications AS (
    SELECT
        patient_id,
        STRING_AGG(DISTINCT medication, ', ') AS medications
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
),

outcomes AS (
    SELECT
        patient_id,
        COALESCE(MAX(readmitted_30d), 0) AS readmitted_30d,
        COALESCE(MAX(in_hospital_death), 0) AS in_hospital_death,
        COALESCE(MAX(icu_admission), 0) AS icu_admission
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
)

SELECT
    d.patient_id,
    d.age,
    d.sex,
    d.bmi,
    d.smoking_status,
    d.alcohol_use,
    d.exercise_level,
    dx.diagnoses,
    l.labs,
    m.medications,
    o.readmitted_30d,
    o.in_hospital_death,
    o.icu_admission

FROM demographics d
LEFT JOIN diagnoses dx ON d.patient_id = dx.patient_id
LEFT JOIN labs l ON d.patient_id = l.patient_id
LEFT JOIN medications m ON d.patient_id = m.patient_id
LEFT JOIN outcomes o ON d.patient_id = o.patient_id
=======
=======
>>>>>>> app-v2
WITH demographics AS (
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
),

diagnoses AS (
    SELECT
        patient_id,
        STRING_AGG(DISTINCT primary_diagnosis, ', ') AS diagnoses
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
),

labs AS (
    SELECT
        patient_id,
        STRING_AGG(DISTINCT test_name, ', ') AS labs
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    WHERE is_abnormal = 1
    GROUP BY patient_id
),

medications AS (
    SELECT
        patient_id,
        STRING_AGG(DISTINCT medication, ', ') AS medications
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
),

outcomes AS (
    SELECT
        patient_id,
        COALESCE(MAX(readmitted_30d), 0) AS readmitted_30d,
        COALESCE(MAX(in_hospital_death), 0) AS in_hospital_death,
        COALESCE(MAX(icu_admission), 0) AS icu_admission
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
)

SELECT
    d.patient_id,
    d.age,
    d.sex,
    d.bmi,
    d.smoking_status,
    d.alcohol_use,
    d.exercise_level,
    dx.diagnoses,
    l.labs,
    m.medications,
    o.readmitted_30d,
    o.in_hospital_death,
    o.icu_admission

FROM demographics d
LEFT JOIN diagnoses dx ON d.patient_id = dx.patient_id
LEFT JOIN labs l ON d.patient_id = l.patient_id
LEFT JOIN medications m ON d.patient_id = m.patient_id
LEFT JOIN outcomes o ON d.patient_id = o.patient_id
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
;