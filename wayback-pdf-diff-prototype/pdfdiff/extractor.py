import fitz

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)
    lines = []

    for page in doc:
        text = page.get_text()
        lines.extend(text.splitlines())

    return lines