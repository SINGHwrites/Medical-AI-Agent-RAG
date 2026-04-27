import os
from pathlib import Path
from groq import Groq

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None

ROOT_DIR = Path(__file__).resolve().parents[2]

if load_dotenv is not None:
    load_dotenv(ROOT_DIR / ".env")

def _get_client():
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set.")
    return Groq(api_key=api_key)

def rewrite_summary_groq(summary):
    client = _get_client()

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
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=120
    )
    return completion.choices[0].message.content.strip()