##Wayback PDF Diff Prototype
Prototype implementation of a backend PDF diff engine designed for the Wayback Machine.
This project explores how differences between two versions of a PDF document can be detected and represented in a structured format. The goal is to eventually support PDF comparison in the Wayback Machine, similar to how HTML page diffs are currently supported.
##Motivation
The Wayback Machine currently supports visual diffing of archived HTML pages.
However, many archived resources are PDF documents, such as:
Research papers
Policy documents
Government reports
Technical documentation
Being able to detect changes between different archived versions of these PDFs would be extremely valuable for:
Researchers
Journalists
Historians
Policy analysts
This prototype demonstrates how a backend system could generate structured diff output for two PDF documents.
##How It Works
The prototype follows a simple pipeline:

PDF Version A
      │
      ▼
Text Extraction (PyMuPDF)
      │
      ▼
Text Normalization
      │
      ▼
Line Comparison (difflib)
      │
      ▼
Structured JSON Diff Output
##Steps:
Extract text from each page of both PDFs using PyMuPDF
Normalize extracted text
Compare the two versions using Python's difflib
Generate structured JSON output showing additions and removals
##Project Structure

wayback-pdf-diff-prototype
│
├── pdfdiff
│   ├── __init__.py
│   ├── extractor.py
│   └── diff_engine.py
│
├── samples
│   ├── capture1.pdf
│   └── capture2.pdf
│
├── run_test.py
├── pyproject.toml
├── setup.py
└── README.md
Main Components
pdfdiff/extractor.py
Handles text extraction from PDF documents.
pdfdiff/diff_engine.py
Performs comparison between two extracted texts and generates structured differences.
run_test.py
Example script demonstrating how to use the package.
##Installation
Clone the repository:

git clone https://github.com/welcomemeet/wayback-pdf-diff-prototype.git
cd wayback-pdf-diff-prototype
Install the package:


pip install .
##Usage Example
Example Python usage:
Python

from pdfdiff import compare
import json

result = compare(
    "samples/capture1.pdf",
    "samples/capture2.pdf"
)

print(json.dumps(result, indent=2))
Example output:
Json

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
This structured JSON output can later be integrated with existing Wayback diff visualization tools.
##Dependencies
Python 3.10+
PyMuPDF
Python standard library (difflib, json)
Prototype Goals
This prototype focuses on demonstrating the backend diff engine.
The final goal is to build a system that:
compares two archived PDF captures
generates structured diff output
integrates with existing Wayback diff infrastructure
##Future improvements may include:
better text normalization
paragraph-level comparison
page-level diff visualization
compatibility with web-monitoring-diff output format
improved handling of multi-page documents
Related Projects
This work is inspired by existing Internet Archive tools such as:
web-monitoring-diff
warcprox
brozzler
Repository
GitHub Repository:

https://github.com/welcomemeet/wayback-pdf-diff-prototype
Author
Meet Darji
GSoC 2026 Applicant — Internet Archive
Future Work
Planned improvements include:
matching the JSON diff format used by web-monitoring-diff
supporting multi-page PDF alignment
improved diff accuracy
integration with Wayback Machine tools
