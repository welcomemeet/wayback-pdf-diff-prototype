# Wayback PDF Diff Prototype

This project explores how differences between two versions of a PDF document could be detected and visualized, inspired by the Wayback Machine "Wayback Changes" system.

The prototype demonstrates a simple pipeline that extracts text from PDFs, compares the content, generates a structured diff output, and visualizes the changes through a browser-based viewer.

## Motivation

The Wayback Machine currently allows users to compare changes between archived HTML pages. However, many archived resources exist as PDF documents (reports, research papers, government documents, etc.). Detecting differences between archived PDF versions would provide valuable insights for researchers, journalists, and historians.

This prototype explores how such functionality might be implemented.

## Prototype Pipeline


PDF Version A
↓
Text Extraction (PyMuPDF)
↓
Diff Detection (Python difflib)
↓
Structured Output (JSON)
↓
HTML Viewer (visual diff display)


## Project Structure


wayback-pdf-diff-prototype
│
├── BACKEND
│ └── pdf_diff_engine.py
│
├── samples
│ ├── capture1.pdf
│ └── capture2.pdf
│
├── viewer
│ └── diff_viewer.html
│
├── backend
│ └── diff.json
│
└── requirements.txt


## How It Works

1. Two PDF documents are provided as input.
2. The Python script extracts text from each PDF using PyMuPDF.
3. The extracted text is compared using Python’s `difflib`.
4. Differences are written to a structured JSON file.
5. The HTML viewer loads the JSON file and highlights added or removed text.

## Running the Prototype

Run the diff engine:


python BACKEND/pdf_diff_engine.py


Start a simple local server:


python -m http.server 8000


Open the viewer in your browser:


http://localhost:8000/viewer/diff_viewer.html


## Technologies Used

- Python
- PyMuPDF
- difflib
- HTML / JavaScript

## Future Improvements

- Support for multi-page PDF comparisons
- Improved semantic comparison
- Side-by-side diff visualization
- Integration with existing Wayback diff systems

## Context

This prototype was developed while preparing a proposal for the Google Summer of Code project:

**"Wayback PDF Changes" – Internet Archive**
