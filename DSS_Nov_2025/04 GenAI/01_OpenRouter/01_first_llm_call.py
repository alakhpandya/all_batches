from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

agent = OpenAI(
    
    base_url="https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)

# response_1 = agent.chat.completions.create(

#     model= "nvidia/nemotron-3-ultra-550b-a55b:free",

#     messages= [
#         {
#             "role" : "user",

#             "content" : "Explain openrouter under 100 words"    
#         }
#     ]
# )

# print("Response from the model:\n", response)
# print("Response from the model:\n", response_1.choices[0].message.content)

print("Royal AI agent is ready to help you! \nWhat can I help you with?\n")
user_prompt = input("[You] :")

response = agent.chat.completions.create(

    model= "nvidia/nemotron-3-ultra-550b-a55b:free",

    messages= [
        {
            "role" : "user",

            "content" : user_prompt    
        }
    ]
)

print("[Royal AI Agent] :", response.choices[0].message.content)