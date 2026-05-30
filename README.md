# Explain Like I'm 5

An AI-powered app that explains any text or PDF at 3 complexity levels:
Kid, Student, and Expert.

## Tech Stack
- FastAPI
- Streamlit  
- Ollama (Mistral)
- pdfplumber

## How to Run
1. Start Ollama: `ollama serve`
2. Start backend: `uvicorn main:app --reload`
3. Start frontend: `streamlit run frontend/app.py`