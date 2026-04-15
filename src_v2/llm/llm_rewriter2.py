from functools import lru_cache

try:
    from transformers import pipeline
except Exception:
    pipeline = None


MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


def _fallback_summary(summary) -> str:
    diagnoses = ", ".join(summary["diagnoses"]) or "no dominant diagnoses"
    labs = ", ".join(summary["labs"]) or "no dominant lab patterns"
    medications = ", ".join(summary["medications"]) or "no dominant medications"
    return (
        f"Matched {summary['count']} patients aged {summary['age_min']} to "
        f"{summary['age_max']}. Common diagnoses include {diagnoses}. "
        f"Common lab findings include {labs}. Common medications include "
        f"{medications}."
    )


def _build_prompt(summary) -> str:
    return f"""
Rewrite this medical summary in two sentences using only data provided:
Patients found: {summary['count']}
Age range: {summary['age_min']}-{summary['age_max']}
Diagnoses: {', '.join(summary['diagnoses'])}
Labs: {', '.join(summary['labs'])}
Medications: {', '.join(summary['medications'])}

Sentence:
"""
#Write a concise detailed cohort-level clinical summary in exact two sentences.
#Do not invent an individual patient or any facts beyond the provided data summary.


@lru_cache(maxsize=1)
def _get_generator():
    if pipeline is None:
        raise RuntimeError("transformers is not available")

    return pipeline(
        "text-generation",
        model=MODEL_NAME,
        max_new_tokens=250,
    )


def rewrite_summary(summary):
    prompt = _build_prompt(summary)

    try:
        output = _get_generator()(prompt, return_full_text=False)[0]["generated_text"]
    except Exception:
        return _fallback_summary(summary)

    answer = output.strip()

    return answer or _fallback_summary(summary)