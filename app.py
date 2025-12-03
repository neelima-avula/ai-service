rom fastapi import FastAPI
from pydantic import BaseModel
from genai import Client
from genai.schema import *

import os

app = FastAPI()

# DO NOT PUT KEY HERE — Railway env will inject it
client = Client(api_key=os.environ["GEMINI_API_KEY"])

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=req.prompt
    )
    return {"reply": response.output_text}