# Dumb It Down For Me

An AI-powered app that explains any text or PDF at 3 complexity levels: Kid, Student, and Expert.

## Live Demo
- Frontend: https://dumb-it-down-for-me.streamlit.app
- Backend API: https://dumb-it-down-api.onrender.com

## Tech Stack
- FastAPI (backend)
- Streamlit (frontend)
- Groq LLM — Llama 3.3 70B
- pdfplumber (PDF extraction)
- Docker + Docker Compose
- Deployed on Render + Streamlit Cloud

## How to Run Locally
1. Add your Groq API key to `backend/.env`:
   `GROQ_API_KEY=your_key_here`
2. Start both services:
   `docker-compose up --build`
3. Open `http://localhost:8501`