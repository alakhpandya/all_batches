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

messages = [
    {
        "role" : "system",

        "content" : "You are a fresher who have just graduated Computer Science Engineering"
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]



response = client.chat.completions.create(

    model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

    messages= messages
)

print("Agent:", response.choices[0].message.content)