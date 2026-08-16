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

def convert_mcp_tools(tools_list):
    openai_tools = []
    for tool in tools_list:
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

    user_prompt = input("[You] : ")

    messages = [
        {
            "role" : "system",

            "content" : """
            You are a helpful AI assistant. 
            To answer the question of the user, first check all the available tools and if there are tools present that can help answering the question then strictly use those tools instead of using your knowledge.
            """
        },
        {
            "role" : "user",

            "content" : user_prompt
            # "content" : "I want you to greet me first by my name (Tanish) and then tell me what will be the answer if I add 15 into 35?"
            # "content" : "What is 25 added to 18?"
            # "content" : "Tell me something about 'nemotron super' LLM?"
        }
    ]

    from mcp import stdio_client

    # obj = stdio_client(server_params)
    # read_stream, write_stream = stdio_client(server_params)         # this operation is not supported outside of "with" block

    async with stdio_client(server_params) as (read_stream, write_stream):
        # print(read_stream)
        # print(write_stream)

        from mcp import ClientSession

        # session = ClientSession(read_stream, write_stream)
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools_list = await session.list_tools()

            # print(type(tools_list), "\n")
            # print(tools_list)

            # print(tools_list.tools)
            # i = 1
            # print("Available tools:")
            # for tool in tools_list.tools:
                # print(f"{i}. {tool.name} - {tool.description}")
                # i += 1

            openai_tools = convert_mcp_tools(tools_list.tools)

            from pprint import pprint
            # pprint(openai_tools)

            # ----------------- LLM Call --------------------
            response = client.chat.completions.create(

                model="nvidia/nemotron-3-super-120b-a12b:free",

                messages=messages,

                tools=openai_tools,

                tool_choice= "auto"

            )

            # print(response)
            tool_calls = response.choices[0].message.tool_calls
            print("\nTool Calls:")
            pprint(tool_calls)
            print()
            if tool_calls:
                # here we will write a logic that will call the necessary tool
                tool = tool_calls[0]
                tool_name = tool.function.name
                print("\nTool name:", tool_name)

                import json
                tool_args = json.loads(tool.function.arguments)
                print("\nTool arguments:", tool_args)

                tool_result = await session.call_tool(
                    tool_name,
                    tool_args
                )

                print("\nTool result:", tool_result)

                # ----------------- Updating Conversation Memory --------------------

                messages.append({
                    "role" : "tool",

                    "tool_call_id" : tool.id,

                    "content" : str(tool_result)
                })

                # ----------------- Final LLM Call --------------------

                final_response = client.chat.completions.create(

                    model="nvidia/nemotron-3-super-120b-a12b:free",

                    messages=messages

                )

                ai_response = final_response.choices[0].message.content
                
            else:
                ai_response = response.choices[0].message.content

            # ----------------- Updating Conversation Memory --------------------
            messages.append({
                "role" : "assistant",

                "content" : ai_response
            })        

            print("\n[Agent] :")
            print(ai_response)

import asyncio
if __name__ == "__main__":
    asyncio.run(main())