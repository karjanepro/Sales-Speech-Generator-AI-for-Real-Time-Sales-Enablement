from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
    
def generate_sales_speech(category, product, client_profile):
    prompt = f"""Write a persuasive sales speech for the following:
    Category: {category}
    Product: {product}
    Client: {client_profile}
    Tone: On-brand, confident, and concise.
    """

    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content.strip()
