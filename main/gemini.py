from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(os.getenv("TEST"))
print(f'printed --------- {GEMINI_API_KEY}')

client = genai.Client(api_key=GEMINI_API_KEY)

def product_name(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate a silly prouct around the theme of {prompt}. Respond with only the product name."
    )
    print(response.text)
    return response.text.strip()