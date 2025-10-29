from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
from PIL import Image
from io import BytesIO
import base64


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def product_name(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate a silly prouct around the theme of {prompt}. Respond with only the product name."
    )
    return response.text.strip()

def procuct_theme(product: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Out of the categories: luxury, minimalist, organic, tech, cartoon 
            which theme suits a product named {product} best. Respond with only one word being the name of the theme."""
    )
    return response.text.strip()

def product_description(product: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Provide a catchy description (2-3 sentences) for a product named {product}. Respond with only the description."
    )
    return response.text.strip()

def product_tagline(product: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Create a memorable tagline for a product named {product}. Respond with only the tagline."
    )
    return response.text.strip()

def product_logo(product: str) -> str:
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=f'Make a logo for a product called {product}. Only make one image, do not include the product name. Make the image size low.',
        config=types.GenerateImagesConfig(
            output_mime_type = "image/jpeg",
            number_of_images= 1,
            personGeneration = "dont_allow"
        )
    )
    data = response.images[0].image_bytes
    b64data = base64.b64encode(data).decode('utf-8')
    data_url = f"data:{response.images[0].mime_type};base64,{b64data}"
    return data_url

def product_slide(product: str, mode: int) -> str:
    if not mode in (0,1,2):
        mode = 0
    version = ['title', 'graphs', 'product mark-up']
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=f'Create a {version[mode]} slide, for a product called {product}. Only return one slide. Make the image size low',
        config=types.GenerateImagesConfig(
            output_mime_type = "image/jpeg",
            number_of_images= 1,
            personGeneration = "dont_allow"
        )
    )
    response.images[0].show()
    data = response.images[0].image_bytes
    image = Image.open(BytesIO(data))
    return image