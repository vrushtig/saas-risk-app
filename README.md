# 🔎 SaaS Contract Risk Analyzer

B2B contracts are long, confusing, and written to protect the vendor.  
This tool reads the fine print for you — and tells you what to worry about.

---

## 💡 What It Does

- Upload a SaaS contract (PDF or TXT)
- Breaks it down clause by clause
- Flags who benefits: vendor / client / neutral
- Scores risk from 0.0 to 1.0
- Suggests how to make each clause better
- Outputs a full contract summary + CSV + JSON

---

## 🧠 How It Works

This isn’t just a prompt — it's a full product pipeline.

- Smart clause segmentation
- Legal clause matching using embeddings
- Evaluated with Gemini 1.5 Pro
- Outputs are structured, transparent, and useful

---

## 🛠 Tech Stack

| Layer           | Tools & Libraries                                                  |
|------------------|-------------------------------------------------------------------|
| Core Language    | Python                                                            |
| UI               | Streamlit                                                         |
| PDF Parsing      | PyMuPDF                                                           |
| Clause Matching  | SentenceTransformers (`MiniLM-L6-v2`) + FAISS                     |
| Clause Evaluation| Google Gemini 1.5 Pro (structured API call with smart prompts)    |
| Summarization    | Pandas + Matplotlib                                               |

---

## 🚀 Try the Live App Here

- https://business-risk-app-for-saas-contracts.streamlit.app

---

## 👋 About Me

I’m Vrushti Gangwal — MSIS Grad @ NYU.  
This started as a capstone, but I built it like a real product because it deserves to exist.


📫 [LinkedIn](www.linkedin.com/in/vrushti-gangwal-3844ab1b3)

https://business-risk-app-for-saas-contracts.streamlit.app
