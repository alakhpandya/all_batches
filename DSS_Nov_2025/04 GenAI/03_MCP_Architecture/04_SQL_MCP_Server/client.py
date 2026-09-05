from dotenv import load_dotenv

from openai import OpenAI

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)

from mcp import ClientSession

import os

import asyncio

import logging

import json

load_dotenv()
client = OpenAI(

    api_key= os.getenv("OPENROUTER_API_KEY"),

    base_url= os.getenv("OPENAI_API_BASE")      # my system env var name

)

# MODEL = os.getenv("OPENAI_MODEL_NAME")    # model name in my system env var (first priority)
MODEL = os.getenv("MODEL_NAME")    # model name var from my .env file
# print("Model:", MODEL)

async def main():
    pass



if __name__ == "__main__":
    asyncio.run(main())