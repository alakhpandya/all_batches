from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# key = os.getenv("OPENROUTER_API_KEY")
# print("API Key:", key)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= os.getenv("OPENROUTER_API_KEY")
)

response = client.chat.completions.create(
    model="google/gemma-4-31b-it:free",
    messages=[
        {
            "role" : "user",
            "content" : "Explain Openrouter in simple language under 100 words"
        }
    ]
)

# Explain openrouter.
# Ans: openrouter is...

print(response.choices[0].message.content)