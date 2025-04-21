import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

golden_df = pd.read_csv("golden_clauses.csv")
texts = golden_df["standard_clause"].tolist()
types = golden_df["clause_type"].tolist()

embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(texts, convert_to_numpy=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
clause_map = {i: {"text": texts[i], "type": types[i]} for i in range(len(texts))}

def retrieve_best_golden_clause(input_clause):
    input_vec = embedder.encode([input_clause])
    D, I = index.search(np.array(input_vec), k=1)
    match = clause_map[I[0][0]]
    return match["type"], match["text"]

def build_rag_prompt(clause_text):
    clause_type, golden_clause = retrieve_best_golden_clause(clause_text)
    return clause_type, f"""
You are an AI contract compliance assistant working on SaaS contracts.

Compare the following client clause to a golden standard clause. Identify if this clause is favorable to the vendor or client, rate the risk (0.0 to 1.0), and recommend specific improvements.

📄 Client Clause:
\"\"\"{clause_text}\"\"\"

📘 Golden Clause:
\"\"\"{golden_clause}\"\"\"

Return ONLY valid JSON with:
- clause_type
- favorability (client / vendor / neutral)
- risk_score
- deviation
- recommendation
"""