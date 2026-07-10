from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

question = input("How can I help you today?\n")

response = client.chat.completions.create(

    model="google/gemma-4-31b-it:free",

    messages=[

        {
            "role": "system",
            "content": """
            You are a professional fitness coach.

            Your job is to:
            - Help users improve fitness
            - Suggest workouts
            - Give diet advice
            - Motivate users
            - Explain in simple language

            Keep answers practical and beginner-friendly.
            """
        },

        {
            "role": "user",
            "content": question
        }

    ],

    temperature=0.7,
    max_tokens=100
)

print("\nAI Fitness Coach:\n")
print(response.choices[0].message.content)