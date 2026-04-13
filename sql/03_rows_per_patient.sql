SELECT AVG(cnt) AS avg_rows_per_patient
FROM (
    SELECT patient_id, COUNT(*) AS cnt
    FROM read_csv_auto('data/raw/merged_patient_data.csv')
    GROUP BY patient_id
);