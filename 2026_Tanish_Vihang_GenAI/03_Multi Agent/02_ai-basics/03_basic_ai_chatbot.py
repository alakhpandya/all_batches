from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
)

question = input("AI Fitness Coach: Hey, I am your fitness coach how may I help you today?\n")

# print("User input:", question)
response = client.chat.completions.create(
    # model="nousresearch/hermes-3-llama-3.1-405b:free",
    # model="google/gemma-4-31b-it:free",
    model="deepseek/deepseek-chat",
    messages= [
        {
            "role" : "system",
            "content" : """
            You are a professional fitness coach.

            Your job is to :
            - help improve overall fitness of your clients
            - suggest workouts
            - provide diet advise
            - motivate your clients
            - explain everything in simple words in form of short answers
            """
        },
        {
            "role" : "user",
            "content" : question
        }
    ],
    temperature=0.7
    # max_tokens=100
)

print("AI Fitness Coach:")
print(response.choices[0].message.content)