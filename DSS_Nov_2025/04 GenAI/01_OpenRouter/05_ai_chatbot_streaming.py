from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

agent = OpenAI(
    
    base_url="https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)


messages = [
    {
        "role" : "system",

        "content" : """
        You are a professional fitness coach. 

        Your job is to:
        - help your client to improve their overall fitness
        - suggest workouts
        - provide diet advice
        - motivate your client

        Explain everything in short and simple language.
        """
    }
]

print('Hey, I am your AI fitness coach! \nAsk me for any help related to your health or type "exit" to end the conversation.\n')

while True:
    user_prompt = input("\n\n[You] : ")

    if user_prompt.lower() == "exit":
        break

    messages.append({
        "role" : "user",

        "content" : user_prompt
    })

    stream = agent.chat.completions.create(

        model= "google/gemma-4-26b-a4b-it:free",

        # model= "nvidia/nemotron-3-ultra-550b-a55b:free",

        messages= messages,

        stream= True
    )

    print("\n\n[AI Fitness Coach]:\n")
    
    ai_response = ""
    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token is not None:
            ai_response = ai_response + token
            print(token, end="", flush=True)
    

    messages.append({
        "role" : "assistant",

        "content" : ai_response
    })