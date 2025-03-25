from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from github_analyzer import extract_skills_from_github
from matcher import match_jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze/{username}")
async def analyze_user(username: str):
    try:
        skills = extract_skills_from_github(username)
        job_matches = match_jobs(skills)
        return {"skills": skills, "matches": job_matches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
