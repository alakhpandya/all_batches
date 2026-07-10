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

    stream = client.chat.completions.create(

        model="google/gemma-4-31b-it:free",

        messages=messages,

        temperature=0.7,
        max_completion_tokens=50,

        stream=True
    )

    full_response = ""

    print("\nCoach: ", end="")

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            token = chunk.choices[0].delta.content
            print(token, end="", flush=True)
            full_response += token

    print("\n")

    messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )