from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

agent = OpenAI(
    
    base_url="https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)

print("Royal AI agent is ready to help you! \nWhat can I help you with?\n")
user_prompt = input("[You] :")

# --------------------- role: system ---------------------
messages = [
    {
        "role" : "system",

        # "content" : "You are a teacher who teaches Computers in a high-school."
        "content" : "You are a Data Scientist who is addressing to IIT students from Computer Engineering field in an event."
    },
    {
        "role" : "user",

        "content" : user_prompt    
    }
]

# --------------------- Few-shot Prompting ---------------------
messages = [
    {
        "role" : "system",

        "content" : "You are a sentiment analysis AI."
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

        "content" : "The food at that place was disgusting"    
    },
    {
        "role" : "assistant",

        "content" : "Negative"
    },
    {
        "role" : "user",

        "content" : "The event was neither great but was not bad as well"    
    },
    {
        "role" : "assistant",

        "content" : "Neutral"
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]

# --------------------- Generating Structured Output ---------------------

messages = [
    {
        "role" : "user",

        "content" : """
        Give me the output in jSon format:

        name
        age
        gender

        Student: Yash, 21, M
        """
    }
]

# --------------------- Multi-turn Conversation/Conversation Memory ---------------------

messages = [
    {
        "role" : "user",
        "content" : "Hi, Priyanshi this side."
    },
    {
        "role" : "assistant",
        "content" : "Hey Priyanshi, what do you want to ask me today?"
    },
    {
        "role" : "user",
        "content" : "I want to write a note on different concepts of Gen AI (each topic under 50 words). Here is the first concept: The difference between an AI Agent & an LLM"
    },
    {
        "role" : "assistant",
        "content" : "Think agent as a human & LLM as its brain."
    },
    {
        "role" : "user",
        "content" : user_prompt
    }
]

messages = [
    {
        "role" : "system",

        "content" : """
        You are a story teller who creates short stories in simple & easy English.
        """
        # You are a story teller who creates short stories of less than 100 words in simple & easy English.
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]

# user_prompt = Write a story on this plot: I was walking on the street that evening.

response = agent.chat.completions.create(

    model= "nvidia/nemotron-3-ultra-550b-a55b:free",

    messages= messages,

    # temperature= 1.9      # maximum possible temperature value

    # we use high value of temperature when we want more creativity e.g, novel writting, poetry etc

    # temperature= 0.0       # minimum possible temperature value - we use this for coding/mathematical prompts

    temperature= 0.7,        # most common - for all the prompts in general, we use 0.5 to 1

    # max_tokens= 130
    
    max_completion_tokens= 130
)

print("[Royal AI Agent] :", response.choices[0].message.content)