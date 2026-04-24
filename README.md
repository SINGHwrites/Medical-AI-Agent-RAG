# Medical AI Agent RAG

Medical AI Agent RAG is a local-first retrieval and summarization project for cohort-style medical questions. It combines:

- rule-based cohort filtering with DuckDB
- semantic search with Sentence Transformers + FAISS
- structured cohort summarization
- optional LLM rewriting with either a local Qwen model or the Groq API
- a Streamlit UI for interactive use

Example queries:

- `obesity death`
- `diabetes kidney elderly`
- `hypertension readmitted`
- `obesity ICU`

## Repository Layout

```text
.
|-- app/
|   `-- streamlit_app.py
|-- docs/
|   |-- readme_v1.md
|   |-- readme_v2.md
|   `-- requirements_v2.txt
|-- sql/
|-- src_v1/
`-- src_v2/
    |-- agent/
    |-- llm/
    |-- retrieval/
    `-- summarizer/
```

## Prerequisites

- Python 3.12 recommended
- `pip`
- Git
- Internet access on first run to download model assets

Optional:

- a Groq API key if you want cloud LLM rewriting

## Required Local Data

The tracked Git repository does not include the large runtime data artifacts. To run the app successfully, place these files in the project under the exact paths below:

- `data/summaries/patient_summary.parquet`
- `data/indexes/patient_embeddings.npy`
- `data/indexes/faiss_index.bin`

Without those files, the retrieval module will fail at startup.

## Setup

Clone the repository and move into the project directory:

```powershell
git clone https://github.com/SINGHwrites/Medical-AI-Agent-RAG.git
cd Medical-AI-Agent-RAG
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell execution policy blocks activation, use:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

## Install

Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

If you want to use Groq rewriting, create a root `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run

### Streamlit UI

Start the web app:

```powershell
streamlit run app/streamlit_app.py
```

Open the local URL shown by Streamlit, typically:

```text
http://localhost:8501
```

How to use it:

- enter a cohort-style medical query
- leave both LLM options unchecked for retrieval + structured summary only
- enable `Use Groq cloud LLM` if `GROQ_API_KEY` is configured
- enable `Use local LLM` to generate a local narrative with `Qwen/Qwen2.5-1.5B-Instruct`

### Terminal Mode

Run the terminal version:

```powershell
python -m src_v2
```

You can still run the module file directly if needed:

```powershell
python src_v2/agent/main.py
```

This mode prompts for a query, prints the structured cohort summary, and then runs the local Qwen rewriter.

## First-Run Downloads

On the first run, the project may download model assets such as:

- `sentence-transformers/all-MiniLM-L6-v2`
- `Qwen/Qwen2.5-1.5B-Instruct` when local LLM mode is used

If the models are already cached locally, later runs can reuse them.

## Troubleshooting

- `ModuleNotFoundError`: make sure the virtual environment is activated and dependencies were installed.
- `File not found` for parquet, numpy, or FAISS assets: verify the required files exist under `data/`.
- Groq errors: confirm `.env` exists in the repository root and contains `GROQ_API_KEY`.
- Slow first run: model downloads and initialization can take time.
- High memory or CPU usage: leave local LLM disabled and use structured evidence only, or use Groq instead.

## Current Notes

- The Streamlit app is the primary entrypoint for this branch.
- `src_v2` contains the active retrieval, summarization, and LLM code.
- `src_v1` is retained as an older implementation for reference.
