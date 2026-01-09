from fastapi import FastAPI, UploadFile, Form
from app.resume_parser import extract_text_from_pdf
from app.jd_parser import extract_keywords
from app.scorer import calculate_ats_score

app = FastAPI(title="ATS Resume Analyzer")

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile,
    job_description: str = Form(...)
):
    # Read resume PDF
    resume_bytes = await resume.read()
    resume_text = extract_text_from_pdf(resume_bytes)

    # Extract skills/keywords
    resume_skills = extract_keywords(resume_text)
    jd_skills = extract_keywords(job_description)

    # Calculate ATS score
    result = calculate_ats_score(
        resume_text,
        job_description,
        resume_skills,
        jd_skills
    )

    return result
