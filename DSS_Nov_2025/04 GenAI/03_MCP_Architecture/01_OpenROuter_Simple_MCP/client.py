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

def convert_mcp_tools(mcp_tools):
    openai_tools = []

    for tool in mcp_tools:

        openai_tools.append({

            "type" : "function",

            "function" : {

                "name" : tool.name,

                "description" : tool.description,

                "parameters" : tool.inputSchema

            }
        })

    return openai_tools


async def main():

    from mcp import stdio_client

    # obj = stdio_client(server_params)
    # print(obj)
    # obj: (read_stream, write_stream)

    # read_stream, write_stream = stdio_client(server_params)           # This operation is not supported outside "with" block
    async with stdio_client(server_params) as (read_stream, write_stream):
        # print(read_stream)
        # print(write_stream)               

        from mcp import ClientSession
        # session = ClientSession(read_stream, write_stream)

        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools_obj = await session.list_tools()

            # print("Available Tools:")
            # print(tools_obj)
            # print(tools_obj.tools)

            # import numpy as np
            # print(np.array(tools_obj.tools))

            from pprint import pprint
            # for tool in tools_obj.tools:
            #     # print(tool) 
            #     print("Name:", tool.name)
            #     print("Description:", tool.description)           
            #     print("Input Schema:")
            #     pprint(tool.inputSchema)
            #     print("\n")

            openai_tools = convert_mcp_tools(tools_obj.tools)

            messages = [
                {
                    "role" : "system",

                    "content" : "You are an AI assistant. Strictly use tools whenever available & needed."
                },
                {
                    "role" : "user",

                    "content" : "What is the answer if 35 is added to 25?"
                }

            ]

            # --------------- LLM Call ---------------
            response = client.chat.completions.create(

                # model= "nvidia/nemotron-3-ultra-550b-a55b:free",
                # model = "openai/gpt-oss-20b:free",
                model = "nvidia/nemotron-3.5-lightning:free",

                messages= messages,

                tools= openai_tools,

                tool_choice= "auto"
            )

            # print(response.choices[0].message)
            msg = response.choices[0].message

            # --------------- Updating conversation memory ---------------
            messages.append(
                msg
            )

            tool_call = msg.tool_calls[0]

            tool_name = tool_call.function.name

            # tool_args = tool_call.function.arguments
            # print(type(tool_args))

            import json
            tool_args = json.loads(
                tool_call.function.arguments
            )

            print("Tool Name:", tool_name)

            print("Tool Args:", tool_args)

            # print("Type:", type(tool_args))

            tool_result = await session.call_tool(
                name = tool_name,
                arguments= tool_args
            )

            print("Tool Output:", tool_result)

            # --------------- Updating conversation memory ---------------
            messages.append({
                "role" : "tool",

                "tool_call_id" : tool_call.id,

                "content" : str(tool_result)
            })

            # --------------- Final LLM Call ---------------
            
            final_response = client.chat.completions.create(

                # model= "nvidia/nemotron-3-ultra-550b-a55b:free",
                # model = "openai/gpt-oss-20b:free",
                model = "nvidia/nemotron-3.5-lightning:free",

                messages= messages
            )

            print("[Agent] :", final_response.choices[0].message.content)


import asyncio
if __name__ == "__main__":
    asyncio.run(main())