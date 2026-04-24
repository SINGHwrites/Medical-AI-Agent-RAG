import sys
from pathlib import Path
import time

# ROOT PATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
from src_v2.retrieval.hybrid_retriever import hybrid_retrieve
from src_v2.summarizer.summary_builder import build_summary
from src_v2.llm.groq_rewriter import rewrite_summary_groq

# PAGE CONFIG
st.set_page_config(page_title="Medical AI Agent v2.2", layout="wide")

# SIDEBAR
st.sidebar.title("Recent Queries")

if "history" not in st.session_state:
    st.session_state.history = []

if "results" not in st.session_state:
    st.session_state.results = []

for q in st.session_state.history[-5:][::-1]:
    st.sidebar.write(f"- {q}")

# TITLE
st.title("Medical AI Agent v2.2")
st.markdown("Hybrid Retrieval + Structured Summary + Optional Local / Cloud Clinical Narrative")

# INPUT
question = st.text_input("Ask medical query:")
use_groq = st.checkbox("Use cloud LLM (Groq)")

# BUTTON
if st.button("Analyze"):

    if not question.strip():
        st.warning("Please enter a medical query.")
        st.stop()

    st.session_state.history.append(question)

    progress = st.progress(0)
    status = st.empty()
    runtime_box = st.empty()

    start_total = time.time()

    # -----------------------------
    # RETRIEVAL
    # -----------------------------
    status.text("Running hybrid retrieval...")
    t1 = time.time()

    df = hybrid_retrieve(question)

    retrieval_time = time.time() - t1

    progress.progress(35)
    runtime_box.info(f"Elapsed after retrieval: {time.time() - start_total:.2f}s")

    if df.empty:
        st.warning("No matching patients found.")
        st.stop()

    # -----------------------------
    # SUMMARY
    # -----------------------------
    status.text("Building structured summary...")
    t2 = time.time()

    summary = build_summary(df)

    summary_time = time.time() - t2

    progress.progress(65)
    runtime_box.info(f"Elapsed after summary: {time.time() - start_total:.2f}s")

    # -----------------------------
    # LLM
    # -----------------------------
    llm_answer = "Clinical narrative disabled."
    llm_time = 0

    if use_groq:
        status.text("Generating clinical narrative...")
        t3 = time.time()

        runtime_box.info(f"LLM started at: {time.time() - start_total:.2f}s")

        try:
            llm_answer = rewrite_summary_groq(summary)

        except Exception as e:
            llm_answer = f"LLM failed: {e}"

        llm_time = time.time() - t3

        runtime_box.info(f"Elapsed after LLM: {time.time() - start_total:.2f}s")

    # -----------------------------
    # COMPLETE
    # -----------------------------
    progress.progress(100)
    status.text("Completed.")

    total_time = time.time() - start_total

    runtime_box.success(f"Total runtime: {total_time:.2f}s")

    # -----------------------------
    # STORE RESULT
    # -----------------------------
    st.session_state.results.insert(0, {
        "query": question,
        "summary": summary,
        "llm": llm_answer,
        "retrieval_time": retrieval_time,
        "summary_time": summary_time,
        "llm_time": llm_time,
        "total_time": total_time
    })

    # -----------------------------
    # ACTIVE MODEL LABEL
    # -----------------------------
    if use_groq:
        st.caption("Model: Groq Cloud")

    else:
        st.caption("Model: None")

    # -----------------------------
    # METRICS
    # -----------------------------
    c1, c2 = st.columns(2)

    c1.metric("Patients Found", summary["count"])
    c2.metric("Age Range", f"{summary['age_min']} - {summary['age_max']}")

    # -----------------------------
    # TIMINGS
    # -----------------------------
    st.subheader("Processing Times")

    tcol1, tcol2, tcol3, tcol4 = st.columns(4)

    tcol1.metric("Retrieval", f"{retrieval_time:.2f}s")
    tcol2.metric("Summary", f"{summary_time:.2f}s")
    tcol3.metric("LLM", f"{llm_time:.2f}s")
    tcol4.metric("Total", f"{total_time:.2f}s")

    # -----------------------------
    # PREVIEW COLUMNS
    # -----------------------------
    preview_cols = [
        "patient_id",
        "diagnoses",
        "labs",
        "medications"
    ]

    # -----------------------------
    # TWO COLUMN LAYOUT
    # -----------------------------
    left, right = st.columns(2)

    with left:
        st.subheader("Structured Evidence")

        st.write("Top diagnoses:")
        for item in summary["diagnoses"]:
            st.write(f"- {item}")

        st.write("Top labs:")
        for item in summary["labs"]:
            st.write(f"- {item}")

        st.write("Top medications:")
        for item in summary["medications"]:
            st.write(f"- {item}")

    with right:
        st.subheader("Clinical Narrative")

        if use_groq:
            st.write(llm_answer)
        else:
            st.info("Enable Groq to generate a clinical narrative.")

    # -----------------------------
    # EXPORT REPORT
    # -----------------------------
    report_text = f"""
Medical AI Agent v2.2 Report

Query:
{question}

Retrieval time: {retrieval_time:.2f}s
Summary time: {summary_time:.2f}s
LLM time: {llm_time:.2f}s

Structured Answer:
Patients found: {summary['count']}
Age range: {summary['age_min']} - {summary['age_max']}

Top diagnoses:
{chr(10).join(summary['diagnoses'])}

Top labs:
{chr(10).join(summary['labs'])}

Top medications:
{chr(10).join(summary['medications'])}

Clinical Narrative:
{llm_answer}
"""

    st.download_button(
        label="Download Report",
        data=report_text,
        file_name=f"medical_report_{question.replace(' ', '_')}.txt",
        mime="text/plain"
    )

    # -----------------------------
    # CSV EXPORT
    # -----------------------------
    csv_data = df[preview_cols].head(50).to_csv(index=False)

    st.download_button(
        label="Download Patients CSV",
        data=csv_data,
        file_name=f"patients_{question.replace(' ', '_')}.csv",
        mime="text/csv"
    )

    # -----------------------------
    # PATIENT TABLE
    # -----------------------------
    with st.expander("Show Retrieved Patients"):
        st.dataframe(
            df[preview_cols].head(10),
            use_container_width=True
        )

    # -----------------------------
    # PREVIOUS RESULTS
    # -----------------------------
    if len(st.session_state.results) > 1:
        st.subheader("Previous Query Results")

        for i, item in enumerate(st.session_state.results[1:4], start=1):
            with st.expander(f"{i}. {item['query']}"):

                st.write(f"Patients found: {item['summary']['count']}")
                st.write(f"Age range: {item['summary']['age_min']} - {item['summary']['age_max']}")

                st.write("Top diagnoses:")
                for d in item["summary"]["diagnoses"]:
                    st.write(f"- {d}")

                st.write("Clinical Narrative:")
                st.write(item["llm"])

                st.write(
                    f"Timing: Retrieval {item['retrieval_time']:.2f}s | "
                    f"Summary {item['summary_time']:.2f}s | "
                    f"LLM {item['llm_time']:.2f}s | "
                    f"Total {item['total_time']:.2f}s"
                )
