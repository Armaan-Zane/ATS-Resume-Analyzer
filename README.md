# ATS Resume Analyzer

An ATS-style Resume Analyzer that compares a resume with a job description and generates a match score out of 100.

## Features
- Upload resume (PDF)
- Paste job description
- ATS score calculation
- Matched and missing skills
- Semantic similarity matching

## Tech Stack
- Python
- FastAPI
- spaCy
- Sentence Transformers

## How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
