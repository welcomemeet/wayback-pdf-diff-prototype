# Wayback PDF Diff Prototype

Prototype implementation of a backend PDF diff engine designed for the Wayback Machine.

This project explores how differences between two versions of a PDF document can be detected and represented in a structured format. The goal is to eventually support PDF comparison in the Wayback Machine similar to how HTML page diffs are currently supported.

---

## Motivation

The Wayback Machine currently supports visual diffing of archived HTML pages.

However, many archived resources are PDF documents such as:

- research papers
- policy documents
- government reports
- technical documentation

Detecting changes between different archived versions of these PDFs would be extremely useful for researchers, journalists, and historians.

This prototype demonstrates a simple backend system that extracts text from two PDFs and detects differences between them.

---

## How It Works

The prototype follows a simple pipeline:
PDF Version A │ ▼ Text Extraction (PyMuPDF) │ ▼ Line Comparison (difflib) │ ▼ Structured JSON Diff Output
Copy code

Steps:

1. Extract text from each page of the PDFs using **PyMuPDF**
2. Normalize the extracted text into lines
3. Compare the two versions using Python's **difflib**
4. Generate structured JSON output showing additions and removals

---

## Project Structure
wayback-pdf-diff-prototype │ ├── pdfdiff │   ├── init.py │   ├── extractor.py │   └── diff_engine.py │ ├── samples │   ├── capture1.pdf │   └── capture2.pdf │ ├── run_test.py └── README.md
Copy code

---

## Example Output

Running the prototype produces structured JSON output:

```json
[
  {
    "type": "removed",
    "text": "The Wayback Machine archives websites and documents."
  },
  {
    "type": "added",
    "text": "The Wayback Machine archives websites."
  }
]
This output can later be integrated with existing Wayback diff visualization tools.
Running the Prototype
Install dependency

pip install pymupdf
Run the test script

python run_test.py
The script compares the two PDFs in the samples folder and prints the detected differences.
Prototype Goal
This prototype focuses on the backend diff engine only.
The final goal is to build a system that:
compares two archived PDF captures
produces structured diff output
integrates with the existing Wayback diff infrastructure
Next Steps
Future improvements include:
matching the JSON format used by web-monitoring-diff
improving text normalization
supporting multi-page document comparison
packaging the project as a pip-installable Python package
integrating with Wayback diff tools
Repository
Prototype repository:
https://github.com/welcomemeet/wayback-pdf-diff-prototype⁠�
Author
Meet Darji
GSoC 2026 Applicant – Internet Archive
