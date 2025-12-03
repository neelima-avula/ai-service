from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-1.5-flash"  # FREE MODEL


class PromptRequest(BaseModel):
    prompt: str


@app.post("/ai")
def ai_response(req: PromptRequest):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": req.prompt}]}
        ]
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        return {"error": response.json()}

    data = response.json()
    reply = data["candidates"][0]["content"]["parts"][0]["text"]

    return {"reply": reply}