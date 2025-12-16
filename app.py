from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

RESTAURANT_CONTEXT = """
You are an AI assistant for **Lotus Veg Restaurant**.

Business Details:
- Location: 123 Park Road, Charlotte, NC
- Working Hours: Mon–Sat 11 AM – 10 PM, Sunday 12 PM – 9 PM
- Contact: +1 (980) 555-1234
- Cuisines: Indian, South Indian, Indo-Chinese
- Delivery Partners: DoorDash, Uber Eats
- Specialties: Biryani, Butter paneer, Masala Dosa
- Reservation Policy: Walk-ins accepted, reservations for groups > 4.
- Offers: Lunch buffet available Mon–Fri ($15.99)
Menu:
- Paneer Biryani – $16.99
- Paneer Butter Masala – $14.99
- Gobi Manchurian – $12.99
- Masala Dosa – $11.99
- Tomato Soup - $6.99
- Veg Soup - $5.99
- Paneer dosa - $10.99
KIDS Menu:
- cheese sticks - $7.99
- Veg Burger - $8.99
- Noodles - $10.99
Vegan:
-Lemon Rice
-Fruit bowl
-Tofu roll
"""

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ai")
def ai_response(req: PromptRequest):
    prompt = f"""
       {RESTAURANT_CONTEXT}

       User message: {req.prompt}

       Respond as the restaurant’s WhatsApp assistant.
       """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # CORRECT RESPONSE PARSING
    reply = completion.choices[0].message.content

    return {"reply": reply}