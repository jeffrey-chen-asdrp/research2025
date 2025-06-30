from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Write me a one paragraph essay on World War II."
        }
    ]
)

print(completion.choices[0].message.content)