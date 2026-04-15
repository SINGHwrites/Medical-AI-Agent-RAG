import sys
from pathlib import Path

# -----------------------------
# ROOT PATH
# -----------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st

from src_v2.retrieval.hybrid_retriever import hybrid_retrieve
from src_v2.summarizer.summary_builder import build_summary
from src_v2.llm.llm_rewriter import rewrite_summary

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Medical AI Agent v2.1",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Recent Queries")

if "history" not in st.session_state:
    st.session_state.history = []

for q in st.session_state.history[-5:][::-1]:
    st.sidebar.write(f"- {q}")

# -----------------------------
# TITLE
# -----------------------------
st.title("Medical AI Agent v2.1")
st.markdown("Hybrid Retrieval + Structured Summary + LLM Clinical Narrative")

# -----------------------------
# INPUT
# -----------------------------
question = st.text_input("Ask medical query:")

# -----------------------------
# BUTTON
# -----------------------------
if st.button("Analyze"):

    if not question.strip():
        st.warning("Please enter a medical query.")
        st.stop()

    # -----------------------------
    # SAVE HISTORY
    # -----------------------------
    st.session_state.history.append(question)

    with st.spinner("Running hybrid retrieval and clinical summarization..."):

        # -----------------------------
        # RETRIEVE
        # -----------------------------
        df = hybrid_retrieve(question)

        if df.empty:
            st.warning("No matching patients found.")
            st.stop()

        # -----------------------------
        # SUMMARY
        # -----------------------------
        summary = build_summary(df)

        # -----------------------------
        # METRICS
        # -----------------------------
        c1, c2 = st.columns(2)
        c1.metric("Patients Found", summary["count"])
        c2.metric("Age Range", f"{summary['age_min']} - {summary['age_max']}")

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

            llm_answer = rewrite_summary(summary)

            st.write(llm_answer)

        # -----------------------------
        # EXPORT REPORT
        # -----------------------------
        report_text = f"""
Medical AI Agent v2.1 Report

Query:
{question}

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
        # PATIENT TABLE
        # -----------------------------
        with st.expander("Show Retrieved Patients"):

            preview_cols = [
                "patient_id",
                "diagnoses",
                "labs",
                "medications"
            ]

            st.dataframe(
                df[preview_cols].head(10),
                use_container_width=True
            )