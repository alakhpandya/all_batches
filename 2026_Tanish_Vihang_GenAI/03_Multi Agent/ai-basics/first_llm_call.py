from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    # api_key=os.getenv("OPENROUTER_API_KEY")
    api_key="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"
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