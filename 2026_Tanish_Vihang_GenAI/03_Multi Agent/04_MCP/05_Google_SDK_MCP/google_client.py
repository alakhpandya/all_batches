from google import genai

gemini_client = genai.Client()
# It automatically reads the "GEMINI_API_KEY" environment variable

# OR if you want to give some other custom name to your API key then:
"""
from dotenv import load_dotenv
import os

load_dotenv()
gemini_client = genai.Client(
    api_key = os.getenv("YOUR_API_KEY_NAME")
)
"""