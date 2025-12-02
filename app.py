import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# 🔥 Read your API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🔥 Create OpenAI client using the key
client = OpenAI(api_key=OPENAI_API_KEY)

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

    result = completion.choices[0].message["content"]
    return {"reply": result}