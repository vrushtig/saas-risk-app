import requests, time, json, pandas as pd
from utils.retriever import build_rag_prompt

def call_gemini(prompt, api_key):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = { "contents": [{ "parts": [{ "text": prompt }] }] }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return None

def evaluate_clauses_rag(clauses, api_key):
    results = []
    for i, clause in enumerate(clauses):
        clause_type, prompt = build_rag_prompt(clause)
        raw = call_gemini(prompt, api_key)
        if raw:
            raw_cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
            try:
                parsed = json.loads(raw_cleaned)
                parsed["original_clause"] = clause
                parsed["retrieved_type"] = clause_type
                results.append(parsed)
            except:
                pass
        time.sleep(25)
    return pd.DataFrame(results)

def generate_summary(df):
    avg_risk = round(df["risk_score"].astype(float).mean(), 2)
    summary = {
        "average_risk_score": avg_risk,
        "favorability_breakdown": df["favorability"].value_counts().to_dict(),
        "total_clauses": len(df)
    }
    return summary