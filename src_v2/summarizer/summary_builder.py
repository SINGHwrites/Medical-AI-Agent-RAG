import pandas as pd

def build_summary(df):
    count = len(df)

    age_min = df["age"].min()
    age_max = df["age"].max()

    diagnosis_text = ",".join(df["diagnoses"].dropna().astype(str))
    top_diagnoses = pd.Series(diagnosis_text.split(",")).str.strip().value_counts().head(5)

    lab_text = ",".join(df["labs"].dropna().astype(str))
    top_labs = pd.Series(lab_text.split(",")).str.strip().value_counts().head(5)

    med_text = ",".join(df["medications"].dropna().astype(str))
    top_meds = pd.Series(med_text.split(",")).str.strip().value_counts().head(5)

    summary = {
        "count": count,
        "age_min": age_min,
        "age_max": age_max,
        "diagnoses": list(top_diagnoses.index),
        "labs": list(top_labs.index),
        "medications": list(top_meds.index)
    }
    return summary