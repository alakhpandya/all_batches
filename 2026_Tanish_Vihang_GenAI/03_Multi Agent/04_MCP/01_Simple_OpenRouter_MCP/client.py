# import server

# print("MCP Agent started...")

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

from mcp import StdioServerParameters

server_params = StdioServerParameters(
    command= "python",
    args= ["server.py"]
)