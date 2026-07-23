from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
)

question = input("[AI Coach]: Hey, I am your AI fitness coach! What do you want to ask me today?\n\n")

response = client.chat.completions.create(

    model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

    messages= [
        {
            "role" : "system",
            "content" : """
            You are a professional fitness coach.

            Your job is to:
            - help improve overall fitness of the clients
            - suggest workouts
            - provide diet advise
            - motivate your clients

            Explain everything in short & in simple words.
            """
        },
        {
            "role" : "user",
            "content" : question
        }
    ],

    temperature= 0.7,        # balanced temperature = balanced creativity

    # max_tokens=140
)

print("[AI Fitness Coach]:", response.choices[0].message.content)