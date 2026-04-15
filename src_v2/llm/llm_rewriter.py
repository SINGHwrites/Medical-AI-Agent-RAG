from transformers import pipeline

generator = pipeline("text-generation",model="Qwen/Qwen2.5-1.5B-Instruct")

def rewrite_summary(summary):
    
    prompt = f"""
Use only this cohort evidence.

Patients found: {summary['count']}
Age range: {summary['age_min']}-{summary['age_max']}
Diagnoses: {', '.join(summary['diagnoses'])}
Labs: {', '.join(summary['labs'])}
Medications: {', '.join(summary['medications'])}

Write exactly 2 clinical sentences.
Do not add facts not listed above. Do not infer drug classes or extra tests.
Write 2 short and concise cohort-level clinical sentences.

Clinical summary:
"""

    output = generator(prompt, max_new_tokens=200)[0]["generated_text"]
    answer = output.split("Clinical summary:")[-1].strip()
    answer = answer.replace("\n", " ")
    sentences = answer.split(". ")
    answer = ". ".join(sentences[:3])

    if not answer.endswith("."):
        answer += "."
    return answer