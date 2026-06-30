from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )


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

    response = client.chat.completions.create(
        # model = "deepseek/deepseek-chat",
        # model = "google/gemini-2.5-flash",
        model = "google/gemma-4-31b-it:free",
        messages= messages,

        max_completion_tokens=300,
        temperature=0.7
    )

    ai_reply = response.choices[0].message.content

    print("AI Coach:", ai_reply)

    messages.append({
        "role" : "assistant",
        "content" : ai_reply
    })


# Sample prompts:
# 1. I want to reduce my weight as fast as possible. I am ready to put all the efforts you will suggest but I want result at earliest. Guide me and give answer under 200 words.
# 2. I forgot to tell you that I am suffering from high blood pressure, should I continue the same plan or you would want to change it? Again, respond under 200 words.