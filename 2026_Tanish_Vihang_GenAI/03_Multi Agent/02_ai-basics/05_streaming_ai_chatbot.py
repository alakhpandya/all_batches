from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

# Structure
"""
- First: System prompt that sets the persona of the LLM
- Continuing (repeating) conversation until user wants to end it
    - User will ask something
    - AI will reply
    - User will again ask something else
    - AI will reply keeping the context same
    - this will keep repeating until user wants to exit
    - The above things should go inside a loop (while True) that breaks when user enters "exit"
- Inside the loop, our conversation memory should keep building up
- Everytime the entire conversation memory should be sent to the LLM
"""
messages = [

    {
        "role": "system",
        "content": """
        You are an expert fitness coach.

        Help users with:
        - weight loss
        - workout routines
        - diet suggestions
        - motivation

        Keep responses simple and practical.
        """
    }

]

print("AI Coach: Hi! What health solution are you looking for?\n(Type 'exit' whenever you want to stop)")


while True:
    
    user_prompt = input("Your turn: ")

    if user_prompt == "exit":
        break


    messages.append({
        "role" : "user",
        "content" : user_prompt
    })

    stream = client.chat.completions.create(
        # model = "deepseek/deepseek-chat",
        model = "google/gemma-4-31b-it:free",
        messages= messages,

        # max_completion_tokens=300,
        temperature=0.7,

        stream = True
    )

    response = ""

    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token is not None:
            print(token, end="", flush=True)
            response = response + token


    print("\n")

    messages.append({
        "role" : "assistant",
        "content" : response
    })


# Sample prompts:
# 1. I want to reduce my weight as fast as possible. I am ready to put all the efforts you will suggest but I want result at earliest. I am sufferring from high blood pressure so keep it in mind.