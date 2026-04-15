# Medical AI Agent RAG v2

## Overview

Hybrid medical retrieval system built from scratch using open-source Python tools.

Supports:

- Structured SQL retrieval
- Semantic vector retrieval
- Hybrid evidence merging
- Deterministic medical summarization
- Optional LLM clinical rewriting

---

## Architecture

Question
↓
Hybrid Retrieval
├── SQL Retrieval
├── FAISS Semantic Retrieval
↓
Evidence Merge
↓
Summary Builder
↓
Optional LLM Rewrite

---

## Folder Structure

src/
├── retrieval/
├── summarizer/
├── llm/
├── agent/

data/
├── raw/
├── summaries/
├── indexes/

sql/

---

## Main Components

### Retrieval

- retriever.py
- vector_retriever.py
- hybrid_retriever.py

### Summary

- summary_builder.py

### LLM

- llm_rewriter.py

### Agent

- main.py

---

## Run Project

Activate environment:

Windows:
.venv\Scripts\activate

Run agent:
python -m src.agent.main

---

## Example Queries

- obesity hypertension readmitted
- diabetes kidney elderly
- metabolic syndrome
- cardiac risk
- hypertension death

---

## Current Retrieval Models

### Structured
DuckDB

### Semantic
SentenceTransformer all-MiniLM-L6-v2
FAISS

### LLM
TinyLlama

---

## Outputs

### Structured Answer
Deterministic medical cohort summary

### LLM Answer
Optional narrative interpretation

---

## Current Version

v2 = Hybrid Retrieval Stable Baseline
