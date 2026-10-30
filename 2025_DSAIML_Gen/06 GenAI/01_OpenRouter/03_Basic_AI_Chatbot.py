from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
agent = OpenAI(

    base_url="https://openrouter.ai/api/v1",
    
    api_key=os.getenv("OPENROUTER_API_KEY")

)

print("Hey, I am your fitness coach!\nAsk me for any help related to your health...\n")
prompt = input("[You] : ")

messages = [
    {
        "role" : "system",

        "content" : """You are a team of a fitness expert, a dietician, a medicine doctor and a nutrtionist. You guide your clients to stay healthy, fit & active by suggesting simple, effective & easy to implement:
        - workouts
        - diet plans
        - motivation
        
        Answer their questions in simple & easy-to-understand English."""
    },
    {
        "role" : "user",

        "content" : prompt
    }
]



response = agent.chat.completions.create(

    model="openrouter/free",     # automatically assigns the best free model available

    messages= messages
)

print("[Agent] :", response.choices[0].message.content)