from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os

from llm import get_all_explanations
from extractor import extract_text_from_pdf, chunk_text

app = FastAPI()

# This allows our Streamlit frontend to talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# For plain text input
class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Explainer API is running!"}

@app.post("/explain/text")
def explain_text(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    chunked = chunk_text(input.text)
    results = get_all_explanations(chunked)
    return results

@app.post("/explain/pdf")
async def explain_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    # Save uploaded PDF temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        text = extract_text_from_pdf(temp_path)
        chunked = chunk_text(text)
        results = get_all_explanations(chunked)
        return results
    finally:
        # Always delete temp file even if error occurs
        os.remove(temp_path)