# ATS Resume Analyzer 🔍

An **ATS-style Resume Analyzer** that compares a candidate’s resume with a job description and generates a **match score out of 100**, closely simulating how real-world Applicant Tracking Systems (ATS) filter resumes.

This project demonstrates **backend engineering, applied NLP, and full-stack development**, and is designed to be **interview-ready and recruiter-friendly**.

---

## 🚀 Features

- Upload resume in **PDF format**
- Paste a **job description**
- Generate an **ATS match score (0–100)**
- View **matched skills** and **missing skills**
- Semantic similarity–based analysis (not just keyword matching)
- Clean and simple **web-based UI**
- Deployed as a **live, shareable web application**

---

## 🧠 How the ATS Scoring Works

The final ATS score is calculated using a **weighted scoring model**, inspired by real ATS systems.

### 🔢 Scoring Breakdown

- **Exact Skill Match (50%)**  
  Matches resume skills against a predefined skill database

- **Semantic Similarity (30%)**  
  Uses NLP sentence embeddings to compare the meaning of the resume and job description

- **Keyword Density & Relevance (20%)**  
  Measures presence of relevant, role-specific terms

### ✅ Final Score Formula

```
ATS Score =
(Exact Skill Match × 0.5)
+ (Semantic Similarity × 0.3)
+ (Keyword Relevance × 0.2)
```

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **spaCy**
- **Sentence Transformers**
- **Jinja2**
- **PyMuPDF**
- **HTML & CSS**

---

## 📂 Project Structure

```
ATS_Resume_Analyzer
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── resume_parser.py
│   ├── jd_parser.py
│   └── scorer.py
├── data
│   └── skills.txt
├── templates
│   └── index.html
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
python -m uvicorn app.main:app --reload
```

### 5️⃣ Open in Browser
```
http://127.0.0.1:8000
```

---

## 📈 Example Output

ATS Score: 72 / 100

Matched Skills: Python, SQL, Git

Missing Skills: Docker, AWS, REST APIs

---

## 🎯 Use Cases

Resume optimization for job applications

Understanding how ATS systems filter resumes

Comparing resumes against different job roles

Interview preparation and skill gap analysis

---

## 🚀 Deployment

The application can be deployed on platforms like Render or Railway using the following start command:

uvicorn app.main:app --host 0.0.0.0 --port 10000

---

## 👤 Author

This project was built to demonstrate:

Backend development

Applied Natural Language Processing

System design thinking

End-to-end project deployment
