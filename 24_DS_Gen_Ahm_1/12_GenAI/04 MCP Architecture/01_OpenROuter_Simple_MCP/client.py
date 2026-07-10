# Flow/Architecture:
"""
                 User
                   │
                   ▼
            OpenRouter LLM
                   │
                Prompt
                   │
                   ▼
              MCP Client
                   │
          session.call_tool()
                   │
                   ▼
              MCP Server
                   │
        Python Function (Tool) Executes
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


import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

server_params = StdioServerParameters(
    command="python",
    args=["server.py"]
)

def convert_mcp_tools(mcp_tools):
    openai_tools = []
    for tool in mcp_tools:
        openai_tools.append(
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                }
            }
        )

    return openai_tools

async def main():

    async with stdio_client(server_params) as (read_stream, write_stream):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            # print("\nAvailable Tools:\n")

            # for tool in tools.tools:
            #     print("Tool Name:", tool.name)
            #     print("Description:\n", tool.description)
            #     print("Input Schema:\n", tool.inputSchema)

            openai_tools = convert_mcp_tools(tools.tools)

            # print("\nOpenAI Tools:\n")
            # print(openai_tools)

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[
                    {
                        "role": "user",
                        "content": "What is 25 added to 18?"
                    }
                ],
                tools=openai_tools,
                tool_choice= "auto"
            )

            message = response.choices[0].message

            # print(message)

            tool_call = message.tool_calls[0]

            tool_name = tool_call.function.name

            tool_args = json.loads(
                tool_call.function.arguments
            )

            print("\n", "Tool Name:", tool_name, "\n")

            print("Tool arguments:", tool_args, "\n")

            tool_result = await session.call_tool(

                tool_name,

                tool_args

            )

            print("\nTool Result:\n", tool_result, "\n")

            # ------------------------ Conversation Memory ------------------------
            messages = [
                {
                    "role": "user",
                    "content": "What is 25 added to 18?"
                },

                message,

                {
                    "role": "tool",

                    "tool_call_id": tool_call.id,

                    "content": str(tool_result)
                }
            ]

            final_response = client.chat.completions.create(

                model="deepseek/deepseek-chat",

                messages=messages
            )

            print("\nFinal Response:\n", final_response.choices[0].message.content)


if __name__ == "__main__":
    asyncio.run(main())