from functools import lru_cache

try:
    import torch
except Exception:
    torch = None

try:
    from transformers import pipeline
except Exception:
    pipeline = None

if torch is not None:
    torch.set_num_threads(4)

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"


def _fallback_summary(summary) -> str:
    diagnoses = ", ".join(summary["diagnoses"]) or "no dominant diagnoses"
    labs = ", ".join(summary["labs"]) or "no dominant lab findings"
    medications = ", ".join(summary["medications"]) or "no dominant medications"
    return (
        f"Matched {summary['count']} patients aged {summary['age_min']} to "
        f"{summary['age_max']}. Common diagnoses include {diagnoses}. "
        f"Common lab findings include {labs}. Common medications include "
        f"{medications}."
    )

# MODEL CACHE
@lru_cache(maxsize=1)
def load_model():
    if pipeline is None:
        raise RuntimeError("transformers is not available")
    return pipeline(
        "text-generation",
        model=MODEL_NAME
    )

# REWRITE FUNCTION
def rewrite_summary(summary):
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

    try:
        generator = load_model()
        output = generator(
            prompt,
            max_new_tokens=60,
            do_sample=False,
            temperature=0.2,
            return_full_text=False
        )[0]["generated_text"]
    except Exception:
        return _fallback_summary(summary)

    answer = output.strip()
    answer = answer.replace("\n", " ")

    sentences = answer.split(". ")
    answer = ". ".join(sentences[:2])

    if not answer.endswith("."):
        answer += "."

    return answer or _fallback_summary(summary)
