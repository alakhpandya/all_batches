from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
    # api_key="your_api_key_here"
)

response = client.chat.completions.create(
        model="google/gemma-4-31b-it:free",
        messages=[
            {
                "role" : "user",
                "content" : "Explain Openrouter in simple words"
            }
        ]
    )

print(response.choices[0].message.content)