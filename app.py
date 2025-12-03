from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-1.5-flash"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):

    url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": req.prompt}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    try:
        response.raise_for_status()
    except:
        return {"error": response.text}

    data = response.json()
    reply = data["candidates"][0]["content"]["parts"][0]["text"]
    return {"reply": reply}