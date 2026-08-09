# import server

# print("Hello World!")

# Flow/Architecture:
"""
    MCP Client will request to List Tools
                   │
                   ▼
MCP Server will respond with list of all tools
                   │
              User Prompt
                   │
                   ▼
           Prompt + Tools list
                   │
                   ▼
             OpenRouter LLM
                   │
                   ▼
               Tool Call
                   │
             Tool Executes
                   │
                   ▼
             Returns Result
                   │
                   ▼
             OpenRouter LLM
                   │
         Generates Final Reply
                   │
                   ▼
                 User
"""

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


async def main():

    from mcp import stdio_client

    # obj = stdio_client(server_params)
    # print(obj)
    # obj: (read_stream, write_stream)

    # read_stream, write_stream = stdio_client(server_params)           # This operation is not supported outside "with" block
    async with stdio_client(server_params) as (read_stream, write_stream):
        # print(read_stream)
        # print(write_stream)               # Now we see a different error because we still need to complete this portion of code

        from mcp import ClientSession
        # session = ClientSession(read_stream, write_stream)

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Available Tools:")
            print(tools)


import asyncio
if __name__ == "__main__":
    asyncio.run(main())