import requests
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_skills_from_github(username: str):
    repos = requests.get(f"https://api.github.com/users/{username}/repos").json()
    collected_text = ""
    for repo in repos:
        readme_url = f"https://raw.githubusercontent.com/{username}/{repo['name']}/main/README.md"
        response = requests.get(readme_url)
        if response.status_code == 200:
            collected_text += response.text + "\n"

    if not collected_text:
        raise Exception("Keine README-Dateien gefunden.")

    prompt = f"Extract the key technical skills and technologies mentioned in the following text:\n{collected_text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts concise lists of tech skills."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip().split(", ")
