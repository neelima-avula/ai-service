from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# Configure Gemini with API Key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")  # works everywhere

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):
    response = model.generate_content(req.prompt)
    return {"reply": response.text}