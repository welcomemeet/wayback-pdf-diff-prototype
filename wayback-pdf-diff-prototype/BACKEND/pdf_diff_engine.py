import fitz
import difflib
import json
import os


def extract_lines(pdf_path):
    doc = fitz.open(pdf_path)
    lines = []

    for page in doc:
        text = page.get_text()
        lines.extend(text.splitlines())

    return lines


def compare_pdfs(pdf1, pdf2):

    old_lines = extract_lines(pdf1)
    new_lines = extract_lines(pdf2)

    diff = difflib.ndiff(old_lines, new_lines)

    results = []
    page = 1

    for line in diff:

        if line.startswith("- "):
            results.append({
                "page": page,
                "type": "removed",
                "text": line[2:]
            })

        elif line.startswith("+ "):
            results.append({
                "page": page,
                "type": "added",
                "text": line[2:]
            })

    return results


if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    pdf1 = os.path.join(BASE_DIR, "samples", "capture1.pdf")
    pdf2 = os.path.join(BASE_DIR, "samples", "capture2.pdf")

    diff = compare_pdfs(pdf1, pdf2)

    output_file = os.path.join(BASE_DIR, "backend", "diff.json")

    with open(output_file, "w") as f:
        json.dump(diff, f, indent=2)

    print("PDF diff generated →", output_file)