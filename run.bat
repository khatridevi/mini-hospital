@echo off
start cmd /k "cd backend && uvicorn main:app --reload"
start cmd /k "streamlit run frontend/app.py"cd