from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": req.prompt}
        ]
    )

    return {"reply": completion.choices[0].message.content[0].text}