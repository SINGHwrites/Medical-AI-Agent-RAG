# Medical AI Agent

A production-oriented medical cohort retrieval and summarization system built from scratch using open-source Python tools.

The project transforms large-scale structured clinical data into an interactive AI-assisted retrieval engine capable of cohort filtering, semantic similarity search, structured evidence summarization, optional LLM clinical narrative generation, and Dockerized production packaging.

---

# Project Objective

The goal of this system is to build a practical medical AI retrieval agent that can answer cohort-level medical questions such as:

- obesity death
- diabetes kidney elderly
- hypertension readmitted
- obesity ICU

The agent retrieves matching patients, summarizes cohort evidence, and optionally generates concise clinical narratives.

---

# End-to-End Architecture

medical-ai-agent/

├── app/

├── src_v2/

├── data/

├── sql/

├── scripts/

├── Dockerfile

---

# Phase 1 — Clinical Data Engineering

Multiple synthetic medical tables were merged into one large unified dataset.

Source tables:
- patients
- diagnoses
- lab_results
- medications
- outcomes

Initial merged dataset characteristics:
- 33,919,890 rows
- 64 columns
- approximately 10 GB

This stage focused on schema control, dtype optimization, and efficient storage design.

---

# Phase 2 — SQL Analytical Layer

DuckDB was selected as the analytical engine because of its local speed and low setup overhead.

Implemented SQL profiling:
- row count
- unique patients
- null profile
- diagnosis prevalence
- lab prevalence
- medication prevalence

Custom SQL queries were created for medical cohort retrieval.

Supported cohort filters:
- obesity
- hypertension
- diabetes
- chronic kidney disease
- ICU admission
- mortality
- readmission
- elderly population

---

# Phase 3 — Patient Summary Construction

A patient-level summary table was created to compress row-level clinical data into retrieval-ready records.

Final summary columns:
- patient_id
- age
- sex
- bmi
- smoking_status
- alcohol_use
- exercise_level
- diagnoses
- labs
- medications
- readmitted_30d
- in_hospital_death
- icu_admission

Summary dataset size:
- 100,000 patient summaries

Storage:
- parquet
- deploy-safe parquet subset

---

# Phase 4 — Hybrid Retrieval Engine

Hybrid retrieval combines:

## SQL retrieval
Fast rule-based cohort filtering using DuckDB.

## Semantic retrieval
Embedding-based similarity search using FAISS.

Embedding model:
all-MiniLM-L6-v2

Vector store:
FAISS index

Hybrid retrieval merges:
- SQL matches
- semantic nearest neighbors

Final result size:
- top 100 patients

---

# Phase 5 — Structured Cohort Summarization

A summary builder converts retrieved patients into structured evidence.

Output includes:
- patient count
- age range
- top diagnoses
- top labs
- top medications

This creates deterministic evidence before LLM generation.

---

# Phase 6 — LLM Layer

Two optional LLM modes were implemented.

## Local LLM
Qwen2.5-1.5B-Instruct

Used for fully local inference.

## Cloud LLM
Groq API

Used for faster inference and lower local CPU load.

Cloud mode is recommended for production.

---

# Phase 7 — Streamlit Application

Interactive application built using Streamlit.

Features:
- query input
- structured evidence display
- optional clinical narrative generation
- retrieval timing
- previous query persistence
- CSV export
- report export

The application supports both local and cloud LLM selection.

---

# Phase 8 — Deployment Dataset Engineering

Full production dataset was too large for lightweight deployment.

A deploy-safe subset was created.

Deploy subset:
- 5000 patient rows
- deploy parquet
- deploy embeddings
- deploy FAISS index

Purpose:
- memory-safe container deployment
- cloud demonstration

---

# Phase 9 — Docker Production Packaging

Application was containerized using Docker.

Docker base:
python:3.11-slim

Container includes:
- Streamlit app
- retrieval engine
- deploy dataset
- cloud LLM integration

## Build

docker build -t medical-ai-agent .

## Run

docker run -p 8501:8501 -e GROQ_API_KEY=YOUR_KEY medical-ai-agent

Validated locally:
- retrieval works
- LLM works
- Streamlit works inside container

---

# Current Technical Status

Completed:
- local full retrieval system
- hybrid retrieval
- local and cloud LLM support
- Streamlit UI
- Docker production image

Stable current release:
v2.3

---

# Future Work

## Cloud Deployment

Planned deployment targets:
- Railway
- Docker cloud container hosting

Cloud work includes:
- container secret management
- persistent production hosting
- cloud inference stability

---

## API Layer

Planned migration:
- FastAPI backend

This enables:
- API-first serving
- frontend separation

---

## Frontend Evolution

Planned frontend:
- React

Possible later:
- dashboard analytics
- richer cohort visualizations

---

## Retrieval Upgrades

Future improvements:
- stronger ranking logic
- semantic reranking
- query intent expansion

---

## LLM Upgrades

Future experiments:
- stronger cloud models
- prompt refinement
- citation-safe cohort generation

---

# Technology Stack

- Python
- DuckDB
- FAISS
- Sentence Transformers
- Streamlit
- Transformers
- Groq API
- Docker

---

# Repository Structure

app/
src_v2/
data/
sql/
scripts/

---

# Development Philosophy

The system was intentionally built incrementally:

data engineering → retrieval → summarization → LLM → UI → Docker

This preserves modularity and allows controlled upgrades.

---

# Next Immediate Milestone

Cloud deployment of Dockerized production container.
