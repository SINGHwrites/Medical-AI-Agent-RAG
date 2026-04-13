# Medical AI Agent RAG

Medical AI Agent RAG is a local prototype for cohort retrieval and summary generation over longitudinal patient data.
It uses DuckDB to transform raw visit-level records into one summary document per patient, then answers free-text clinical questions by:

1. retrieving matching patient summaries
2. aggregating the matched cohort
3. optionally rewriting the structured result into natural language with a local language model

The current implementation is closer to a lightweight retrieval + summarization pipeline than a full vector-search RAG stack. Retrieval is keyword-driven over a patient summary parquet file, and the repository already includes placeholders for future indexing work.

## Quick Start

If the raw dataset already exists at `data/raw/merged_patient_data.csv`, run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src_v1/build_full_patient_summary.py
python -m src_v2
```

Then enter a question such as:

- `elderly patients with diabetes`
- `hypertension and readmitted`
- `kidney patients with icu`

## Current workflow

The project is organized around the following data flow:

```text
Raw patient CSV
-> DuckDB profiling queries
-> patient-level summary table
-> summary CSV / parquet
-> question-to-filter retrieval
-> cohort summary
-> optional LLM rewrite
```

## Repository layout

```text
Medical AI Agent RAG/
|- configs/                 # reserved for configuration files
|- data/
|  |- indexes/              # reserved for future vector / retrieval indexes
|  |- processed/            # reserved for intermediate processed assets
|  |- raw/                  # source dataset
|  |- summaries/            # patient-level retrieval corpus
|- notebooks/               # exploratory notebooks
|- outputs/                 # saved SQL profiling outputs
|- sql/                     # DuckDB SQL scripts
|- src_v1/                  # legacy flat scripts
|- src_v2/                  # current modular application
|- tests/                   # test placeholder
|- requirements.txt
|- schema.md
```

## Code structure

### `src_v2` (current app)

`src_v2` is the active implementation and should be treated as the main application code.

- `agent/main.py`: command-line entry point
- `retrieval/retriever.py`: maps question keywords to DuckDB filters over `data/summaries/patient_summary.parquet`
- `summarizer/summary_builder.py`: converts a matched cohort into a structured summary
- `llm/llm_rewriter.py`: rewrites that structured output into concise prose using a local `transformers` pipeline with a fallback template
- `__main__.py`: enables `python -m src_v2`

### `src_v1` (legacy helpers)

`src_v1` contains earlier standalone scripts that are still useful operationally:

- `run_sql.py`: runs profiling queries and writes CSV outputs into `outputs/`
- `build_patient_summary.py`: exports a sample patient summary file
- `build_full_patient_summary.py`: builds the full patient summary CSV and parquet used by retrieval
- `ask.py`: older interactive retrieval script

## Data expectations

The repository expects the raw source file at:

```text
data/raw/merged_patient_data.csv
```

The derived retrieval corpus is written to:

```text
data/summaries/patient_summary.csv
data/summaries/patient_summary.parquet
```

Based on the current profiling outputs, the dataset is large and longitudinal:

- around 33.9 million rows
- 100,000 unique patients
- 64 columns
- multiple rows per patient due to visits, labs, medications, and outcomes over time

## Patient summary design

The patient-level summary object keeps only the information needed for retrieval and cohort summarization:

- demographics
- lifestyle factors
- diagnoses
- abnormal labs
- active medications
- outcomes such as ICU admission, death, and readmission

The aggregation logic in `sql/11_patient_summary.sql` compresses many time-series rows into one retrieval document per patient.

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Core packages used by the project:

- `duckdb` for query execution over CSV/parquet
- `pandas` and `pyarrow` for tabular processing and parquet output
- `transformers` and `torch` for optional local text generation
- Jupyter packages for notebook-based exploration

## Build the retrieval corpus

### 1. Run data profiling queries

This executes the SQL scripts in `sql/01` through `sql/10` and writes CSV snapshots to `outputs/`.

```powershell
python src_v1/run_sql.py
```

### 2. Build the full patient summary dataset

This executes `sql/11_patient_summary.sql` and writes both CSV and parquet outputs to `data/summaries/`.

```powershell
python src_v1/build_full_patient_summary.py
```

If you only want a preview file instead of the full build:

```powershell
python src_v1/build_patient_summary.py
```

## Run the interactive agent

After building `data/summaries/patient_summary.parquet`, start the modular app with:

```powershell
python -m src_v2
```

You will be prompted for a medical query such as:

- `elderly patients with diabetes`
- `hypertension and readmitted`
- `kidney patients with icu`

The app will:

1. retrieve a matching cohort from the patient summary parquet
2. print a structured cohort summary
3. print a rewritten natural-language answer

## Retrieval behavior

The current retriever is rule-based. It does not yet use embeddings or semantic search.

Supported keyword patterns currently include:

- elderly / old -> `age > 70`
- diabetes -> diagnosis contains `type2_diabetes`
- kidney / creatinine -> labs contain `creatinine`
- hypertension -> diagnosis contains `hypertension`
- obesity -> diagnosis contains `obesity`
- readmitted -> `readmitted_30d = 1`
- icu -> `icu_admission = 1`
- death -> `in_hospital_death = 1`

This means the quality of answers currently depends on:

- the quality of the patient summary aggregation
- the exact keyword mappings in `src_v2/retrieval/retriever.py`
- the completeness of the diagnoses, labs, and medication strings in the summary corpus

## LLM behavior

The LLM rewrite step uses:

```text
TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

If the `transformers` pipeline or model load fails, the application falls back to a deterministic template summary. This keeps the app usable even when the model is unavailable.

## SQL scripts

The `sql/` directory is split into three broad groups:

- `01` to `10`: profiling and domain-specific inspection queries
- `11`: patient-level summary aggregation
- `12` to `14`: example cohort queries

The corresponding CSV outputs are stored in `outputs/`.

## Project status

What is already in place:

- raw longitudinal patient dataset
- DuckDB-based summarization workflow
- patient-level retrieval corpus in parquet format
- interactive cohort query flow
- optional local LLM rewrite

What is not yet fully implemented:

- vector embeddings
- semantic retrieval
- populated retrieval indexes in `data/indexes/`
- automated tests
- complete documentation for notebooks and configs

## Notes for contributors

- treat `src_v2` as the primary application code
- treat `src_v1` as legacy utility scripts unless you are intentionally refactoring them
- keep large generated artifacts out of version control
- the repository currently contains minimal project metadata, so clear docstrings and small focused changes will help

## Known cleanup opportunities

- move exploratory notebooks into `notebooks/`
- remove checked-in `__pycache__` artifacts from source folders
- add tests for retrieval rules and summary generation
- centralize configuration rather than keeping paths hard-coded in scripts
- document the dataset schema more formally beyond `schema.md`
