<<<<<<< HEAD
<<<<<<< HEAD
SELECT
    patient_id,
    MAX(readmitted_30d) AS readmitted_30d,
    MAX(in_hospital_death) AS in_hospital_death,
    MAX(icu_admission) AS icu_admission
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
=======
=======
>>>>>>> app-v2
SELECT
    patient_id,
    MAX(readmitted_30d) AS readmitted_30d,
    MAX(in_hospital_death) AS in_hospital_death,
    MAX(icu_admission) AS icu_admission
FROM read_csv_auto('data/raw/merged_patient_data.csv')
GROUP BY patient_id
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
LIMIT 20;