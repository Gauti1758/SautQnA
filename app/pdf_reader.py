import fitz  # PyMuPDF
import re

def extract_qa_pairs_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    print("\n🔍 Extracted Raw Text:\n", text)

    # Normalize: remove extra newlines and join broken lines
    # Replace patterns like "س :" or "س :" with unified format "س:"
    text = re.sub(r"\s*:\s*", ":", text)  
    lines = [line.strip() for line in text.strip().split("\n") if line.strip()]

    # Join lines to reconstruct Q&A blocks
    combined_text = " ".join(lines)

    # Use regex to extract all Q&A pairs
    pattern = r"س:(.*?)ج:(.*?)(?=س:|$)"
    matches = re.findall(pattern, combined_text, re.DOTALL)

    qa_pairs = [(q.strip(), a.strip()) for q, a in matches]

    print(f"\n✅ Found {len(qa_pairs)} Q&A pairs")
    for i, (q, a) in enumerate(qa_pairs, 1):
        print(f"\nQ{i}: {q}\nA{i}: {a}")

    return qa_pairs
