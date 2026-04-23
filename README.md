# Medical AI Agent v2.4

## Overview

Medical AI Agent is an end-to-end clinical cohort retrieval and summarization system built from scratch using open-source Python tools.

The system supports:
- SQL-based cohort retrieval
- Hybrid semantic retrieval using FAISS
- Structured cohort summarization
- Optional local or cloud LLM clinical narrative generation
- Streamlit interactive application
- Docker production containerization

---

## Project Architecture

medical-ai-agent/
├── app/
├── src_v2/
├── data/
├── sql/
├── scripts/
├── Dockerfile

---

## Phase 1 — Data Engineering

Large synthetic clinical dataset was merged from multiple tables:

- patients
- diagnoses
- labs
- medications
- outcomes

Final merged dataset:
- 33.9 million rows
- 64 columns
- ~10GB source size

A deploy-safe reduced cohort dataset was later created:
- 5000 rows
- 13 summary columns

---

## Phase 2 — SQL Cohort Engine

DuckDB was used for fast local analytical retrieval.

Supported query concepts:
- obesity
- hypertension
- diabetes
- kidney
- icu
- death
- readmitted
- elderly

---

## Phase 3 — Patient Summary Layer

Patient-level summary dataset created:

Columns:
- patient_id
- demographics
- diagnoses
- labs
- medications
- outcomes

Stored as:
- parquet
- deploy parquet subset

---

## Phase 4 — Hybrid Retrieval

Hybrid retrieval combines:

### SQL retrieval
DuckDB cohort filtering

### Semantic retrieval
FAISS vector similarity using sentence-transformers

Embedding model:
all-MiniLM-L6-v2

---

## Phase 5 — Structured Summary Builder

Output:
- patient count
- age range
- top diagnoses
- top labs
- top medications

---

## Phase 6 — LLM Layer

Two LLM modes supported:

### Local LLM
Qwen2.5-1.5B-Instruct

### Cloud LLM
Groq API

Cloud mode recommended for production.

---

## Phase 7 — Streamlit Application

Interactive UI includes:
- query input
- retrieval timing
- summary display
- optional LLM generation
- CSV export
- report export
- previous query history

---

## Phase 8 — Deploy Dataset Preparation

Full dataset too large for cloud deployment.

Created deploy-safe subset:
- 5000-row parquet
- deploy embeddings
- deploy FAISS index

---

## Phase 9 — Docker Production Packaging

Dockerized application using:

- python:3.11-slim
- requirements.txt
- deploy-only data folder

Build:

docker build -t medical-ai-agent .

Run:

docker run -p 8501:8501 -e GROQ_API_KEY=YOUR_KEY medical-ai-agent

---

## Local Docker Result

Validated:
- retrieval works
- LLM works
- Streamlit works inside container

---

## Current Status

Stable local production container completed.

---

## Next Work

### Cloud Deployment

Planned targets:
- Railway
- Docker cloud hosting

Future work:
- production cloud secrets
- persistent cloud inference
- API layer
- optional React frontend

---

## Tech Stack

- Python
- DuckDB
- FAISS
- Sentence Transformers
- Streamlit
- Transformers
- Groq API
- Docker

---

## Version

Current release:
v2.4
