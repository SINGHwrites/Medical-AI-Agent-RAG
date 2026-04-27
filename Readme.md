# Medical AI Agent

Production-oriented clinical cohort retrieval and summarization system built from scratch using structured medical data, hybrid retrieval, optional LLM reasoning, and Dockerized deployment.

This project converts large synthetic clinical datasets into an interactive AI-assisted retrieval engine capable of:

- cohort-level SQL filtering  
- semantic patient retrieval  
- structured medical evidence summarization  
- optional LLM-generated cohort narratives  
- local production container execution  

---

# Current Status

✅ Hybrid retrieval working  
✅ Streamlit application working  
✅ Optional local/cloud LLM working  
✅ Docker image built and validated locally  
✅ Deploy-safe dataset prepared  

🔜 Next milestone: cloud deployment

---

# Problem This Project Solves

Medical datasets are usually large, fragmented, and difficult to query interactively.

This system allows natural cohort-style questions such as:

- obesity death  
- diabetes kidney elderly  
- hypertension readmitted  
- obesity icu  

The agent retrieves matching patients, summarizes cohort evidence, and optionally generates concise clinical narratives.

---

# Architecture

Raw Clinical Tables  
↓  
Patient Summary Engineering  
↓  
DuckDB Cohort Retrieval  
↓  
FAISS Semantic Retrieval  
↓  
Structured Summary Builder  
↓  
Optional LLM Layer  
↓  
Streamlit Application  
↓  
Docker Production Container  
↓  
Cloud Deployment (next)

---

# Repository Structure

```text
medical-ai-agent/
├── app/              # Streamlit interface  
├── src_v2/           # Retrieval, summarization, LLM modules  
├── scripts/          # Deploy dataset preparation scripts  
├── sql/              # SQL profiling and cohort queries  
├── data/             # summaries, deploy subsets, FAISS assets  
├── Dockerfile        # production container  
├── README.md  
````

---

# Phase 1 — Clinical Data Engineering

Multiple synthetic medical tables were merged:

* patients
* diagnoses
* lab_results
* medications
* outcomes

Initial full dataset:

* 33,919,890 rows
* 64 columns
* ~10 GB

Main challenge:

Large-scale schema handling for local analytical use.

---

# Phase 2 — SQL Cohort Retrieval Layer

DuckDB is used for fast analytical retrieval.

Supported cohort filters include:

* obesity
* hypertension
* diabetes
* chronic kidney disease
* ICU admission
* mortality
* readmission
* elderly

DuckDB chosen because it enables local analytical performance without external database setup.

---

# Phase 3 — Patient Summary Layer

Row-level data was compressed into patient-level summaries.

Final summary columns:

* patient_id
* age
* sex
* bmi
* smoking_status
* alcohol_use
* exercise_level
* diagnoses
* labs
* medications
* readmitted_30d
* in_hospital_death
* icu_admission

Summary size:

* 100,000 patient summaries

Storage format:

* parquet

---

# Phase 4 — Hybrid Retrieval Engine

Hybrid retrieval combines:

## SQL Retrieval

Rule-based cohort filtering using DuckDB.

## Semantic Retrieval

FAISS nearest-neighbor search using embeddings.

Embedding model:

all-MiniLM-L6-v2

Vector store:

FAISS index

Hybrid output:

* SQL cohort matches
* semantic nearest neighbors
* duplicate removal
* top 100 final patients

---

# Phase 5 — Structured Summary Builder

Retrieved patients are converted into deterministic cohort evidence.

Output includes:

* patient count
* age range
* top diagnoses
* top labs
* top medications

This stage prevents unsupported LLM generation.

---

# Phase 6 — LLM Layer

Two inference modes supported.

## Local LLM

Qwen2.5-1.5B-Instruct

Advantages:

* fully local
* no API dependency

Limitations:

* slower on CPU

---

## Cloud LLM

Groq API

Advantages:

* much faster inference
* cleaner user interaction

Current recommended production mode:

Groq

---

# Phase 7 — Streamlit Application

Interactive UI features:

* medical query input
* structured cohort evidence
* optional LLM generation
* live timing metrics
* previous query persistence
* CSV export
* report export

---

# Phase 8 — Deployment Dataset Optimization

Full dataset was too large for lightweight deployment.

Deploy subset created:

* 5000 rows
* reduced parquet
* deploy embeddings
* deploy FAISS index

Purpose:

Fit memory constraints during deployment.

---

# Phase 9 — Docker Production Packaging

Dockerized with:

python:3.11-slim

Includes:

* Streamlit app
* retrieval engine
* deploy dataset
* optional cloud LLM

---

# Docker Build

```bash
docker build -t medical-ai-agent .
```

---

# Docker Run

```bash
docker run -p 8501:8501 -e GROQ_API_KEY=YOUR_KEY medical-ai-agent
```

---

# Docker Validation

Validated locally:

✅ retrieval works
✅ Streamlit works
✅ Groq LLM works inside container

---

# Current Tech Stack

* Python
* DuckDB
* FAISS
* Sentence Transformers
* Streamlit
* Transformers
* Groq API
* Docker

---

# Active Branches

main → full development history

deploy-prod → deploy-safe production branch

---

# Next Work

## Cloud Deployment

Planned targets:

* Railway
* Docker cloud hosting

Includes:

* environment secret management
* persistent cloud inference
* production runtime validation

---

## API Layer

Planned:

FastAPI backend

This enables:

* API serving
* frontend decoupling

---

## Frontend Evolution

Possible future:

* React frontend
* richer cohort dashboards

---

## Retrieval Improvements

Future upgrades:

* semantic reranking
* better intent expansion
* stronger retrieval ranking

---

# Development Philosophy

The system was intentionally built incrementally:

data engineering → retrieval → summarization → LLM → UI → Docker

This keeps each layer independently testable and replaceable.

---

# Current Release

v2.4

```
```
