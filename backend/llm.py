import os
import requests
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
API_URL = os.getenv("API_URL", "http://localhost:8000")

PROMPTS = {
    "kid": """You are explaining to a 5 year old child. 
    Use very simple words, fun analogies, and short sentences. 
    Avoid any technical terms completely.""",
    
    "student": """You are explaining to a university student. 
    Use clear language, some technical terms are okay, 
    but always explain them. Use examples.""",
    
    "expert": """You are explaining to a domain expert. 
    Be precise, use technical terminology, 
    focus on nuances and deeper insights."""
}

def get_explanation(text: str, level: str) -> str:
    system_prompt = PROMPTS[level]
    
    response = requests.post(
        GROQ_URL,
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Explain this:\n\n{text}"}
            ]
        }
    )
    
    print("GROQ RESPONSE:", response.json())  # add this line
    return response.json()['choices'][0]['message']['content']

def get_all_explanations(text: str) -> dict:
    return {
        "kid": get_explanation(text, "kid"),
        "student": get_explanation(text, "student"),
        "expert": get_explanation(text, "expert")
    }