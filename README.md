Wayback PDF Diff Prototype

This project explores how differences between two versions of a PDF document can be detected and visualized.
It is inspired by the Wayback Machine "Wayback Changes" system, which currently supports comparison of archived HTML pages.

The goal of this prototype is to demonstrate how PDF documents could also be compared, enabling users to identify changes between archived PDF captures.

Motivation

The Wayback Machine archives billions of webpages and documents. While it provides tools to compare changes in HTML pages, many archived resources exist as PDF documents, such as:

government reports

research papers

policy documents

institutional publications

Being able to detect changes between different archived versions of these documents would help researchers, journalists, and historians track document updates over time.

This prototype demonstrates a simple approach for PDF diff detection and visualization.

Prototype Pipeline
PDF Version A
      ↓
Text Extraction (PyMuPDF)
      ↓
Diff Detection (Python difflib)
      ↓
Structured Output (JSON)
      ↓
HTML Diff Viewer

The system extracts text from two PDFs, detects differences, generates structured change data, and visualizes the changes through a browser-based viewer.

Project Structure
wayback-pdf-diff-prototype
│
├── BACKEND
│   └── pdf_diff_engine.py
│
├── samples
│   ├── capture1.pdf
│   └── capture2.pdf
│
├── viewer
│   └── diff_viewer.html
│
├── backend
│   └── diff.json
│
├── requirements.txt
└── README.md
Folder Description

BACKEND

Contains the Python script responsible for:

extracting text from PDFs

detecting differences between documents

generating structured diff output

samples

Example PDF files used to demonstrate the comparison.

viewer

A simple HTML interface that reads the generated JSON diff file and displays changes visually.

backend/diff.json

Stores the structured diff results produced by the Python script.

Installation

Clone the repository:

git clone https://github.com/welcomemeet/wayback-pdf-diff-prototype.git
cd wayback-pdf-diff-prototype

Install required dependencies:

pip install -r requirements.txt
Running the Prototype
Step 1 — Generate the diff

Run the Python script:

python BACKEND/pdf_diff_engine.py

This will generate a file:

backend/diff.json

containing detected differences between the two PDFs.

Step 2 — Start a local server

Run:

python -m http.server 8000
Step 3 — Open the viewer

Open the following URL in your browser:

http://localhost:8000/viewer/diff_viewer.html

You will see highlighted differences between the two PDF documents.

Example Diff Output

Example detected differences:

Page 1

REMOVED:
Internet Archive preserves digital knowledge.

ADDED:
Internet Archive preserves global digital knowledge.

The viewer highlights:

Removed text

Added text

to help users quickly identify document changes.

Technologies Used

Python

PyMuPDF

difflib

HTML / JavaScript

Future Improvements

Possible improvements include:

multi-page PDF comparison

improved semantic text comparison

side-by-side diff visualization

support for scanned PDFs using OCR

integration with existing Wayback diff infrastructure

Context

This prototype was developed while preparing a proposal for the Google Summer of Code project:

Wayback PDF Changes — Internet Archive

The idea is to extend the Wayback Machine diff capabilities so that PDF documents can also be compared across archived versions.

License

This project is licensed under the MIT License.
