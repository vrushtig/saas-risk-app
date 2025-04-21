import fitz  # PyMuPDF
import re

def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    else:
        raise ValueError("Unsupported file type")

def smart_clause_split(text):
    text = re.sub(r'\n+', '\n', text.strip())
    section_splits = re.split(r'\n(?=(\d{1,2}\.|\d{1,2}\.\d{1,2}|[A-Z]\.|\n[A-Z ]{4,}))', text)
    merged = []
    current = ""
    for chunk in section_splits:
        if len(chunk.strip()) < 3:
            continue
        if chunk.strip()[0].isdigit() or chunk.strip().isupper():
            if current:
                merged.append(current.strip())
            current = chunk
        else:
            current += " " + chunk
    if current:
        merged.append(current.strip())
    return [c for c in merged if len(c) > 100]