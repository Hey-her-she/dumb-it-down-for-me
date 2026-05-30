import ollama

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
    
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": f"Explain this:\n\n{text}"
            }
        ]
    )
    
    return response['message']['content']

def get_all_explanations(text: str) -> dict:
    return {
        "kid": get_explanation(text, "kid"),
        "student": get_explanation(text, "student"),
        "expert": get_explanation(text, "expert")
    }