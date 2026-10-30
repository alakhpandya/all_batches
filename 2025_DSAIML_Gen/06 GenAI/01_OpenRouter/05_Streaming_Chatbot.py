from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
agent = OpenAI(

    base_url="https://openrouter.ai/api/v1",
    
    api_key=os.getenv("OPENROUTER_API_KEY")

)

messages = [
    {
        "role" : "system",

        "content" : """You are a team of a fitness expert, a dietician, a medicine doctor and a nutrtionist. You guide your clients to stay healthy, fit & active by suggesting simple, effective & easy to implement:
        - workouts
        - diet plans
        - motivation
        
        Answer their questions in simple & easy-to-understand English."""
    }
]

print("Hey, I am your fitness coach!\nAsk me for any help related to your health...\nDuring the chat, enter 'x' whenever you want to quit.")

while True:
    prompt = input("[You] : ")
    if prompt.lower() == "x":
        break

    messages.append({
            "role" : "user",
    
            "content" : prompt
    })

    stream = agent.chat.completions.create(

        model = "openrouter/free",

        messages = messages,

        stream = True
    )

    print("[AI Fitness Coach] :")

    ai_response = ""
    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token is not None:
            ai_response = ai_response + token
            print(token, end="", flush=True)
    


    messages.append({
        "role" : "assistant",

        "content" : ai_response
    })
