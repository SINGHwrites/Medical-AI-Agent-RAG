import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

# FORCE ROOT .env LOAD
ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

# READ KEY
api_key = os.getenv("GROQ_API_KEY", "").strip()

# CLIENT
client = Groq(api_key=api_key)

def rewrite_summary_groq(summary):

    prompt = f"""
Use only this cohort evidence.

Patients found: {summary['count']}
Age range: {summary['age_min']}-{summary['age_max']}
Diagnoses: {', '.join(summary['diagnoses'])}
Labs: {', '.join(summary['labs'])}
Medications: {', '.join(summary['medications'])}

Write exactly 2 concise clinical cohort sentences.
Do not add unsupported facts.
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content.strip()

