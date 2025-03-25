import json
import os

def match_jobs(skills):
    # Absoluten Pfad zur Datei berechnen
    base_path = os.path.dirname(os.path.abspath(__file__))
    jobs_file = os.path.join(base_path, "job_data.json")

    with open(jobs_file, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    matches = []
    for job in jobs:
        match_score = len(set(job['required_skills']) & set(skills)) / len(job['required_skills'])
        if match_score > 0.3:
            job["match_score"] = round(match_score * 100, 1)
            matches.append(job)
    return sorted(matches, key=lambda x: x["match_score"], reverse=True)
