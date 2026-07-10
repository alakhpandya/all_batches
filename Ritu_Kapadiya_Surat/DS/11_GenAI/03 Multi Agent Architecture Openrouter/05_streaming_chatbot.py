from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
)

print("[AI Coach]: Hey, I am your AI fitness coach! What do you want to ask me today?\n(Type 'exit' whenever you want to stop)")

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
    user_prompt = input("\n[You]: ")

    if user_prompt.lower() == "exit":
        break

    messages.append({
        "role" : "user",
        "content" : user_prompt
    })

    stream = client.chat.completions.create(

        model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",

        messages= messages,

        temperature= 0.7,        # balanced temperature = balanced creativity

        stream= True
    )

    print("[AI Fitness Coach]:")

    response = ""
    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token is not None:
            response = response + token
            print(token, end="", flush=True)

    messages.append({
        "role" : "assistant",
        "content" : response
    })