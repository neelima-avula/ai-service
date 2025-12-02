from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

XAI_API_KEY = os.getenv("XAI_API_KEY")
XAI_URL = "https://api.x.ai/v1/chat/completions"

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai-grok")
def ai_grok(req: PromptRequest):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {XAI_API_KEY}"
    }

    body = {
        "model": "grok-2",      # or grok-beta
        "messages": [
            {"role": "user", "content": req.prompt}
        ]
    }

    res = requests.post(XAI_URL, headers=headers, json=body)

    if res.status_code != 200:
        return {"error": res.json()}

    reply = res.json()["choices"][0]["message"]["content"]
    return {"reply": reply}