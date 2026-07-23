from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
)

# print("Welcome to Ritu AI, how can I help you today?")
# user_prompt = input("You: ")

user_prompt = "Explain Generative AI under 100 words."
# user_prompt = input("Statement to analyse sentiment:\n")

messages_1 = [
    {
        "role" : "system",

        "content" : "You are a fresher who have just graduated Computer Science Engineering"
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]

# Few-shot Prompting
messages_2 = [
    {
        "role" : "system",

        "content" : "You are a sentiment analysis AI"
    },
    {
        "role" : "user",

        "content" : "I loved this movie!"
    },
    {
        "role" : "assistant",

        "content" : "Positive"
    },    
    {
        "role" : "user",

        "content" : "The performance was terrible"
    },
    {
        "role" : "assistant",

        "content" : "Negative"
    },    
    {
        "role" : "user",

        "content" : "The food was OK, it was not that bad but also not great."
    },
    {
        "role" : "assistant",

        "content" : "Neutral"
    }
]

# Prompt that tells LLM to generate "Structured Output"
messages_3 = [
    {
        "role" : "user",
        "content" : """
        Give the information in the json format:

        name
        age
        course

        Student: Ritu, 24, Data Science
        """
    }
]

# Multi-turn conversation (eg, chatbot or simply a conversation that is a series of chats between user & LLM)/Conversation Memory
messages_4 = [
    {
        "role" : "user",
        "content" : "Hi, Ritu this side!"
    },
    {
        "role" : "assistant",
        "content" : "Hi Ritu!"
    },
    {
        "role" : "user",
        "content" : "I want to create a note for each concept of Gen AI in one sentence (under 50 words). Here is the first concept: Tell me what is the role of LLM for an AI agent."
    },
    {
        "role" : "assistant",
        "content" : "Think LLM as a brain of an AI Agent that provides all the thinking ability to the agent."
    },
    {
        "role" : "user",
        "content" : "Ok, would you similarly explain what are tools?"
    }
]


# prompt = "Write a 100-word story on this plot: I was walking on the street that evening."
prompt = "Write a story on this plot: I was walking on the street that evening."

messages = [
    {
        "role" : "system",

        "content" : "You are a student studying in grade 7"
    },
    {
        "role" : "user",
        
        "content" : prompt
    }
]

response = client.chat.completions.create(

    model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

    messages= messages,

    # temperature= 0.0      # low temperature = no creativity - used for coding/math related prompt/problems
    # temperature= 1.0        # high temperature = high creativity - used in novel writing, poem writing etc
    temperature= 0.7,        # balanced temperature = balanced creativity

    max_tokens=140
)

print("Agent:", response.choices[0].message.content)