from google import genai
from mcp import StdioServerParameters, ClientSession
import asyncio
from mcp.client.stdio import stdio_client

# 1. Initialize the official Google GenAI Client
# It automatically reads the GEMINI_API_KEY environment variable
gemini_client = genai.Client()

async def run_agent():
    # Define connection configuration to our local Python MCP Server
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    print("[Agent]: Initializing the connection to the MCP server...")
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
