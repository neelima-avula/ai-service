from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# Load API key from Railway environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY environment variable not set in Railway!")

genai.configure(api_key=api_key)

# Correct Gemini model name for current stable API
model = genai.GenerativeModel("gemini-1.5-flash")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):
    try:
        result = model.generate_content(req.prompt)
        return {"reply": result.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def health():
    return {"status": "ok"}