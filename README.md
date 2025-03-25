
# 🚀 SkillSync – Dein smarter Karriere-Matcher

**SkillSync** ist ein intelligentes Open-Source-Tool, das deine technischen Skills (z. B. von GitHub) automatisch analysiert und mit passenden Jobs matched – inkl. Skill-Empfehlungen und Job-Vorschlägen.

---

## 🌍 ENGLISH

**SkillSync** is a smart, open-source career matcher that analyzes your technical skills (e.g. from GitHub) and matches them with relevant job profiles – with recommendations and insights.

---

## 🎯 Features

- 🔍 Automatische Analyse deines GitHub-Profils
- 🧠 AI-gestützte Extraktion technischer Fähigkeiten (OpenAI API)
- 📄 Vergleiche deine Skills mit offenen Jobprofilen
- 📊 Match-Scores für jedes Jobangebot
- 🧩 Erweiterbar & Open Source

---

## ⚙️ Tech Stack

- **Backend**: Python, FastAPI, OpenAI API, GitHub API
- **Matching**: JSON-basierte Jobdatenbank, NLP
- **Frontend**: (Optional – coming soon)

---

## 🚀 Quickstart

```bash
git clone https://github.com/dein-nutzername/skillsync.git
cd skillsync/backend

# Virtuelle Umgebung erstellen
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/macOS

# Abhängigkeiten installieren
pip install -r requirements.txt

# .env Datei anlegen
echo OPENAI_API_KEY=dein_api_key > .env

# Server starten
uvicorn main:app --reload
```

Dann im Browser öffnen: [http://localhost:8000/analyze/dein_username](http://localhost:8000/analyze/dein_username)

---

## 📁 Projektstruktur

```
skillsync/
├── backend/
│   ├── main.py              # FastAPI REST-API
│   ├── github_analyzer.py   # Skills aus GitHub lesen (per OpenAI)
│   ├── matcher.py           # Matching-Logik mit Scoring
│   ├── job_data.json        # Beispielhafte Job-Datenbank
│   ├── .env                 # API-Key einfügen
│   └── requirements.txt     # Python Dependencies
└── setup_skillsync.bat      # Automatischer Installer für Windows
```

---

## 🤖 Beispiel-API

`GET /analyze/{username}` → Gibt deine extrahierten Skills + passende Job-Matches zurück.

---

## 🛠 API Key Hinweis

Die OpenAI API wird benötigt – kostenlos generierbar unter:  
👉 https://platform.openai.com/account/api-keys

Trage den Schlüssel in `.env` ein:

```env
OPENAI_API_KEY=sk-...
```

---

## 💡 Inspiration

Dieses Tool wurde entwickelt, um Entwickler:innen zu helfen, ihr Potenzial zu erkennen und schneller passende Jobs zu finden – durch moderne AI und praktische Automatisierung.

---

## 🧠 Ideen für die Zukunft

- 🖥 Web-Frontend mit React
- 🌐 LinkedIn-Skill-Matching
- 📚 Lernpfade für empfohlene Skills
- 🧩 Plugin-System für neue Quellen (Devpost, XING etc.)

---

## 📜 Lizenz

MIT License – kostenlos & offen für alle.

---

**Made with ❤️ for Devs & Recruiter.**
