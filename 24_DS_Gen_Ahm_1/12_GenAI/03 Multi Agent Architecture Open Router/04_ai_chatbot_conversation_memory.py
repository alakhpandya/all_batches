from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

messages = [

    {
        "role": "system",
        "content": """
        You are an expert fitness coach.

        Help users with:
        - weight loss
        - workout routines
        - diet suggestions
        - motivation

        Keep responses simple and practical.
        """
    }

]

print("AI Fitness Coach Started!")
print("Type 'exit' to stop.\n")

while True:

    user_input = input("Your turn: ")

    if user_input.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(

        model="google/gemma-4-31b-it:free",

        messages=messages,

        temperature=0.7,
        max_completion_tokens=50
    )

    ai_reply = response.choices[0].message.content

    print("\nCoach:", ai_reply, "\n")

    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )