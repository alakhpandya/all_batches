from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

agent = OpenAI(
    
    base_url="https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)

print("Hey, I am your AI fitness coach! \nAsk me for any help related to your health...\n")
user_prompt = input("[You] :")

messages = [
    {
        "role" : "system",

        "content" : """
        You are a professional fitness coach. 

        Your job is to:
        - help your client to improve their overall fitness
        - suggest workouts
        - provide diet advice
        - motivate your client

        Explain everything in short and simple language.
        """
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]

response = agent.chat.completions.create(

    model= "google/gemma-4-26b-a4b-it:free",

    messages= messages

)

print("[AI Fitness Coach] :", response.choices[0].message.content)