from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
)

print("[AI Coach]: Hey, I am your AI fitness coach! What do you want to ask me today?\n(Type 'exit' whenever you want to stop)\n")

messages= [
    {
        "role" : "system",
        "content" : """
        You are a professional fitness coach.

        Your job is to:
        - help improve overall fitness of the clients
        - suggest workouts
        - provide diet advise
        - motivate your clients

        Explain everything in short & in simple words.
        """
    }
]

while True:
    user_prompt = input("[You]: ")

    if user_prompt.lower() == "exit":
        break

    messages.append({
        "role" : "user",
        "content" : user_prompt
    })

    response = client.chat.completions.create(

        model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

        messages= messages,

        temperature= 0.7        # balanced temperature = balanced creativity

        # max_tokens=140
    )

    ai_reply = response.choices[0].message.content
    print("[AI Fitness Coach]:", ai_reply)

    messages.append({
        "role" : "assistant",
        "content" : ai_reply
    })