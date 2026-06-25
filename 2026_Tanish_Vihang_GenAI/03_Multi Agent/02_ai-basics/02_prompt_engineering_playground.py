from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

# user_prompt = "Explain Artifical Intelligence"
user_prompt = "Write an essay that starts with: Today is the convocation ceremony at my college..."

message_1 = [
    {
        "role" : "system",
        # "content" : "You are explaining to the students of grade-5"
        # "content" : "You are giving a speech to a Data Science conclave."
        "content" : "You have just completed your engineering degree"
    },
    {
        "role" : "user",
        "content" : user_prompt
    }
]

# Few-shot Prompting
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
        "content" : "The performance was terrible"
    },
    {
        "role" : "assistant",
        "content" : "negative"
    },
    {
        "role" : "user",
        "content" : "That politician is a joke"
    }
]

# Prompt that tells LLM to generate "Structured Output"
message_3 = [
    {
        "role" : "user",
        "content" : """
        Give the information in the json format:

        name
        age
        course

        Student: Tanish, 22, Data Science
        """
    }
]

# Multi-turn conversation (eg, chatbot or simply a conversation that is a series of chats between user & LLM)/Conversation Memory
message = [
    {
        "role" : "user",
        "content" : "Hi, Vihang this side!"
    },
    {
        "role" : "assistant",
        "content" : "Hi Vihang!"
    },
    {
        "role" : "user",
        "content" : "I want to create a note for each concept of Gen AI in one sentence (under 50 words). Tell me what is the role of LLM in an AI agent."
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

response = client.chat.completions.create(
    # model="nousresearch/hermes-3-llama-3.1-405b:free",
    # model="google/gemma-4-31b-it:free",
    model="deepseek/deepseek-chat",
    messages=message

    # temperature=0.1
    # temperature=1.5,

    # max_tokens=135,
    # max_tokens=400
)

# print(response)
print(response.choices[0].message.content)