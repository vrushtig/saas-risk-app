import streamlit as st
from utils.clause_extraction import extract_text, smart_clause_split
from utils.clause_evaluator import evaluate_clauses_rag, generate_summary

st.set_page_config(page_title="📄 SaaS Contract Risk Assessor", layout="wide")
st.title("📄 SaaS Contract Risk Analyzer")

uploaded_file = st.file_uploader("Upload your contract (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Extracting clauses..."):
        text = extract_text(uploaded_file)
        clauses = smart_clause_split(text)
        st.success(f"{len(clauses)} clauses extracted")

    with st.spinner("Analyzing with Gemini..."):
        df = evaluate_clauses_rag(clauses, api_key=st.secrets["GEMINI_API_KEY"])
        required_cols = ["retrieved_type", "favorability", "risk_score", "deviation", "recommendation"]
        for col in required_cols:
            if col not in df.columns:
                df[col] = "N/A"
        df["deviation"] = df["deviation"].astype(str)
        df["recommendation"] = df["recommendation"].astype(str)

    st.subheader("📊 Clause-Level Analysis")
    st.dataframe(df)

    st.subheader("📋 Contract Summary")
    df["risk_score"] = df["risk_score"].astype(float)
    summary = generate_summary(df)
    st.json(summary)

    st.download_button("Download Results CSV", df.to_csv(index=False), file_name="contract_analysis.csv")