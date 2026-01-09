from sentence_transformers import SentenceTransformer, util

# Load semantic similarity model
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_ats_score(resume_text, jd_text, resume_skills, jd_skills):
    """
    Calculates ATS score out of 100 using:
    - Skill match (50%)
    - Semantic similarity (30%)
    - Keyword density (20%)
    """

    # 1. Exact skill matching (50 points)
    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(resume_skills & jd_skills) / len(jd_skills)) * 50

    # 2. Semantic similarity (30 points)
    embeddings = model.encode([resume_text, jd_text], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    semantic_score = similarity * 30

    # 3. Keyword density (20 points)
    keyword_score = min(len(resume_skills) / 20, 1) * 20

    final_score = round(skill_score + semantic_score + keyword_score, 2)

    return {
        "ats_score": final_score,
        "matched_skills": sorted(list(resume_skills & jd_skills)),
        "missing_skills": sorted(list(jd_skills - resume_skills))
    }
