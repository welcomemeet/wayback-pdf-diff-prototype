import difflib
from .extractor import extract_text

def compare(pdf1, pdf2):

    old_lines = extract_text(pdf1)
    new_lines = extract_text(pdf2)

    diff = difflib.ndiff(old_lines, new_lines)

    results = []

    for line in diff:

        if line.startswith("- "):
            results.append({
                "type": "removed",
                "text": line[2:]
            })

        elif line.startswith("+ "):
            results.append({
                "type": "added",
                "text": line[2:]
            })

    return results