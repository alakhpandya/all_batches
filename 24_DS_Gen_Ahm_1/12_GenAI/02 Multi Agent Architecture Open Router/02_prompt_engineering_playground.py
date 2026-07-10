# Let's now move from "how to call LLM" to "how to control LLM"...
# Topics we will study:
# System Prompt
# User Prompt
# Temperture:
#     Yesterday I saw an elephant. It was ____
#     high probability tokens: {giant, huge, large, wild, trunk, tusk} = tokens with probability > 0.95 for low temperature
#     high probability tokens: {giant, huge, large, wild, trunk, tusk, amazing, creature, animal, toy} = tokens with probability > 0.85 for low temperature
# Max Tokens
# Message Roles
# Few-shot Prompting
# Structuring the output
# Context Window

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

user_prompt = "Explain Artificial Intelligence"

message_1 = [
        {
            "role": "system",
            "content": "You are an exper Data Scientist with 5 years of experience in companies like Microsoft, Nvidea etc. and majorly working in area of AI research."
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

# Few Shot Prompting example prompt
message_2 = [
    {
        "role" : "system",
        "content" : "You are a sentiment analysis AI"
    },
    {
        "role" : "user",
        "content" : "I love this movie"
    },
    {
        "role" : "assistant",
        "content" : "positive"
    },
    {
        "role" : "user",
        "content" : "The food was terrible"
    },
    {
        "role" : "assistant",
        "content" : "negative"
    },
    {
        "role" : "user",
        # "content" : "The party was awesome"
        "content" : "Water boils at 100 degrees Celsius."
    }
]

# Prompts that tell the LLM to generate "structured output"
message_3 = [
    {
        "role" : "user",
        "content" : """
        Give the student information in json format:
        
        name
        age
        course

        Student: Parth, 21, Data Science
        """
    }
]

# Multi-turn Conversation (eg, chatbot)
message_4 = [
    {
        "role" :"user",
        "content" : "My name is Marmik"
    },
    {
        "role" : "assistant",
        "content" : "Hi Marmik!"
    },
    # {
    #     "role" : "user",
    #     "content" : "What is my name?"
    # }
    {
        "role" : "user",
        "content" : "Hello, I am Alakh"
    }
]

response = client.chat.completions.create(

    model="google/gemma-4-31b-it:free",

    messages=message_4,

    temperature=0.5,
    max_tokens=20

)

print(response.choices[0].message.content)