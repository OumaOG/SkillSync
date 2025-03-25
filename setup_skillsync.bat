@echo off
setlocal enabledelayedexpansion

:: Projektstruktur
mkdir backend

:: Dateien erstellen (werden gleich ersetzt)
echo Erstelle Backend-Dateien...

:: Virtuelle Umgebung + Setup
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

echo ---------------------------------
echo ✅ SkillSync Backend ist bereit!
echo ---------------------------------
echo Starte mit:
echo uvicorn main:app --reload
pause
