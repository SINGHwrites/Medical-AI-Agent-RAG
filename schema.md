<<<<<<< HEAD
<<<<<<< HEAD
| Domain       | Keep                                    | Why                     |
| ------------ | --------------------------------------- | ----------------------- |
| Demographics | age, sex, bmi                           | stable patient identity |
| Lifestyle    | smoking, alcohol, exercise              | risk context            |
| Diagnoses    | primary diagnosis, ICD10, comorbidities | disease core            |
| Labs         | abnormal tests + values                 | strongest signal        |
| Medications  | active meds                             | treatment signal        |
| Outcomes     | ICU, death, readmission                 | target outcomes         |

===================================================
| Field               | Rule                      |
| ------------------- | ------------------------- |
| Dates               | summarize, not list fully |
| repeated labs       | aggregate                 |
| repeated meds       | deduplicate               |
| secondary diagnoses | compress                  |
---------------------------------------------------

=============================================
Correct patient summary should become
---------------------------------------------
Patient 10231
Male 67 BMI 31
Hypertension Diabetes CKD
Abnormal Labs: HbA1c high, Creatinine high
Medications: Metformin, Losartan
Readmitted: Yes

This is what embeddings later should see.

=============================================
Final aggregation rule per domain
---------------------------------------------
-Demographics
Take first stable value.
-Diagnoses
Take unique diagnoses only.
-Labs
Keep abnormal tests first.
-Medications
Unique active meds only.
-Outcomes
Single final summary.

================================
Final Patient Object Shape
--------------------------------
Each patient should become:

Patient P0001503
Age 67 Female BMI 29.4
Lifestyle: former smoker, light alcohol, sedentary
Diagnoses: hypertension, type2_diabetes
Abnormal Labs: HbA1c, glucose_fasting, LDL
Medications: Metformin, Losartan
Outcome: readmitted yes, icu no, death no
----------------------------------------------------
This becomes the future retrieval document.


====================================================
100k patients
↓
100k summaries
↓
100k embeddings later

====================================
Validation Result -> summary is strong because:

|   Component      |        Status             |
|----------------------------------------------|
|  demographics    |    stable                 |
|  diagnoses       |    compressed correctly   |
|  labs	           |    clinically relevant    |
|  medications	   |    deduplicated           |
=======
=======
>>>>>>> app-v2
| Domain       | Keep                                    | Why                     |
| ------------ | --------------------------------------- | ----------------------- |
| Demographics | age, sex, bmi                           | stable patient identity |
| Lifestyle    | smoking, alcohol, exercise              | risk context            |
| Diagnoses    | primary diagnosis, ICD10, comorbidities | disease core            |
| Labs         | abnormal tests + values                 | strongest signal        |
| Medications  | active meds                             | treatment signal        |
| Outcomes     | ICU, death, readmission                 | target outcomes         |

===================================================
| Field               | Rule                      |
| ------------------- | ------------------------- |
| Dates               | summarize, not list fully |
| repeated labs       | aggregate                 |
| repeated meds       | deduplicate               |
| secondary diagnoses | compress                  |
---------------------------------------------------

=============================================
Correct patient summary should become
---------------------------------------------
Patient 10231
Male 67 BMI 31
Hypertension Diabetes CKD
Abnormal Labs: HbA1c high, Creatinine high
Medications: Metformin, Losartan
Readmitted: Yes

This is what embeddings later should see.

=============================================
Final aggregation rule per domain
---------------------------------------------
-Demographics
Take first stable value.
-Diagnoses
Take unique diagnoses only.
-Labs
Keep abnormal tests first.
-Medications
Unique active meds only.
-Outcomes
Single final summary.

================================
Final Patient Object Shape
--------------------------------
Each patient should become:

Patient P0001503
Age 67 Female BMI 29.4
Lifestyle: former smoker, light alcohol, sedentary
Diagnoses: hypertension, type2_diabetes
Abnormal Labs: HbA1c, glucose_fasting, LDL
Medications: Metformin, Losartan
Outcome: readmitted yes, icu no, death no
----------------------------------------------------
This becomes the future retrieval document.


====================================================
100k patients
↓
100k summaries
↓
100k embeddings later

====================================
Validation Result -> summary is strong because:

|   Component      |        Status             |
|----------------------------------------------|
|  demographics    |    stable                 |
|  diagnoses       |    compressed correctly   |
|  labs	           |    clinically relevant    |
|  medications	   |    deduplicated           |
<<<<<<< HEAD
>>>>>>> aab3ca2 (Initial project import)
=======
>>>>>>> app-v2
|  outcomes	       |    normalized             |