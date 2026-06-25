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


while True:
    
    if user_prompt == "exit":
        break