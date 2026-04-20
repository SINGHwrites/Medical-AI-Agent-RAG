import torch
from transformers import pipeline
from functools import lru_cache

# CPU threading
torch.set_num_threads(4)

# MODEL CACHE
@lru_cache(maxsize=1)
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct"
    )

# REWRITE FUNCTION
def rewrite_summary(summary):

    generator = load_model()

    prompt = f"""
Use only this cohort evidence.

Patients found: {summary['count']}
Age range: {summary['age_min']}-{summary['age_max']}
Diagnoses: {', '.join(summary['diagnoses'])}
Labs: {', '.join(summary['labs'])}
Medications: {', '.join(summary['medications'])}

Write exactly 2 concise cohort-level clinical sentences.
Do not add facts not listed above.

Clinical summary:
"""

    output = generator(
        prompt,
        max_new_tokens=60,
        do_sample=False,
        temperature=0.2,
        return_full_text=False
    )[0]["generated_text"]

    answer = output.strip()
    answer = answer.replace("\n", " ")

    sentences = answer.split(". ")
    answer = ". ".join(sentences[:2])

    if not answer.endswith("."):
        answer += "."

    return answer