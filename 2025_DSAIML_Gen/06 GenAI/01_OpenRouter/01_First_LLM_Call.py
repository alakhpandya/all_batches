from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
agent = OpenAI(

    base_url="https://openrouter.ai/api/v1",
    
    api_key=os.getenv("OPENROUTER_API_KEY")

)
print("Agent created successfully...")


# prompt = "Explain what is openrouter under 100 words"
print("Hi! I am your new AI assistant, ask me anything!")
prompt = input("[You] : ")

response = agent.chat.completions.create(

    # model="nvidia/nemotron-3.5-lightning:free",
    # model="openrouter/free",
    model="google/gemma-4-31b-it:free",

    messages=[
        {
            "role" : "user",

            "content" : prompt
        }
    ]
)

# print(response)
print("[Agent] :", response.choices[0].message.content)