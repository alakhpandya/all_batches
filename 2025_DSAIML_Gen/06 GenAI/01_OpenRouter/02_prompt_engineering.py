from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
agent = OpenAI(

    base_url="https://openrouter.ai/api/v1",
    
    api_key=os.getenv("OPENROUTER_API_KEY")

)


# ------------------------- "role" : "system" -------------------------

"""
response = agent.chat.completions.create(
    
        # model="google/gemma-4-31b-it:free",
        # model="deepseek/deepseek-v4.1-flash",
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
    
        messages=[
            {
                "role" : "system",

                "content" : "You are a teacher who teaches computers to grade-5 students."
            },
            {
                "role" : "user",

                "content" : "Explain me what is data science under 200 words."
            }
        ]

    )

# print("Response:", response.choices[0].message.content)
"""

print("Royal AI Agent is ready to help you!\nWhat can I help you with today?\n")
prompt = input("[You] : ")

messages=[
    {
        "role" : "system",

        # "content" : "You are a teacher who teaches computers to grade-5 students."
        "content" : "You are an experienced software engineer with 10 years of industry experience."
    },
    {
        "role" : "user",

        # "content" : "Explain me what is data science under 200 words."
        "content" : prompt
    }
]

# ------------------------- Few shot prompting -------------------------

messages = [
    {
        "role" : "system",

        "content" : "You are a sentiment analyst AI"
    },
    {
        "role" : "user",

        "content" : "I loved that movie!"
    },
    {
        "role" : "assistant",

        "content" : "Positive"
    },
    {
        "role" : "user",

        "content" : "The food at this restaurant is terrible."
    },
    {
        "role" : "assistant",

        "content" : "Negative"
    },
        {
        "role" : "user",

        "content" : "The play at the theatre was ok"
    },
    {
        "role" : "assistant",

        "content" : "Neutral"
    },
    {
        "role" : "user",

        "content" : prompt
    }
]


response = agent.chat.completions.create(

    model="nvidia/nemotron-3-ultra-550b-a55b:free",

    messages= messages

)

print("[Agent] :", response.choices[0].message.content)
