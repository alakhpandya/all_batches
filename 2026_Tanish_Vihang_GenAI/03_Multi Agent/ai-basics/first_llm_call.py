from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

response = client.chat.completions.create(
    # model="nousresearch/hermes-3-llama-3.1-405b:free"
    model="google/gemma-4-31b-it:free",
    messages=[
        {
            "role" : "user",
            "content" : "Explain Openrouter in simple words"
        }
    ]
)

print(response)