from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# NEW MODEL THAT IS GUARANTEED TO WORK
model = genai.GenerativeModel("gemini-1.5-flash")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):
    response = model.generate_content(req.prompt)
    return {"reply": response.text}