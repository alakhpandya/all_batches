import asyncio

from mcp import StdioServerParameters
from mcp.client.session_group import ClientSessionGroup
from openai import OpenAI
from dotenv import load_dotenv
import json
import os
from pprint import pprint

# ---------------- LLM Client ---------------- 

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ---------------- Server Parameters ---------------- 

calculator_server = StdioServerParameters(
    command="python",
    args=["calculator_server.py"]
)

student_server = StdioServerParameters(
    command="python",
    args=["student_server.py"]
)

attendance_server = StdioServerParameters(
    command="python",
    args=["attendance_server.py"]
)

# ---------------- Function to conver mcp tools in a format that is compatible to OpenAI SDK ---------------- 

def convert_mcp_tools(mcp_tools):
    openai_tools = []
    for tool in mcp_tools:
        openai_tools.append(
            {
                "type": "function",
                "function": {
                    "name": mcp_tools[tool].name,
                    "description": mcp_tools[tool].description,
                    "parameters": mcp_tools[tool].inputSchema
                }
            }
        )

    return openai_tools

async def main():

    async with ClientSessionGroup() as group:

        await group.connect_to_server(calculator_server)
        await group.connect_to_server(student_server)
        await group.connect_to_server(attendance_server)

        print("\nAvailable Tools:\n")
        # print(group.tools)
        for tool_name in group.tools:

            print(tool_name)

        # In a real-world application, here an LLM will decide which tool tobe called based on the user prompt
        openai_tools = convert_mcp_tools(group.tools)

        # pprint(openai_tools)
        messages = [
            {
                "role": "system",
                "content": """
                You are an intelligent AI assistant.

                Use tools whenever needed.
                """
            }
        ]

        print("Multi-MCP AI Agent Started!")
        print("Type 'exit' to stop.\n")

        # ---------------- CHAT LOOP ---------------- 

        while True:

            user_input = input("You: ")

            if user_input.lower() == "exit":
                break

            messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            # FIRST API CALL
            response = client.chat.completions.create(

                model="deepseek/deepseek-chat",

                messages=messages,

                tools= openai_tools,

                tool_choice="auto"
            )

            # print(response)
            response_message = response.choices[0].message

            # TOOL EXECUTION
            if response_message.tool_calls:

                # --------------- Storing Tool Call Request in the Conversation Memory ---------------
                messages.append(
                    response_message
                )


                tool_call = response_message.tool_calls[0]
                print("response_message.tool_calls:", response_message.tool_calls)

                function_name = tool_call.function.name

                arguments = json.loads(tool_call.function.arguments)

                result = await group.call_tool(         

                    function_name,

                    arguments

                )

                # print("\nTool Result:\n")
                # print(result.content[0].text)
                
                tool_result = result.content[0].text

                # --------------- Storing Tool Outcome (Result) in the Conversation Memory ---------------
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result
                    }
                )

                # --------------- Second API Call ---------------

                second_response = client.chat.completions.create(

                    model="deepseek/deepseek-chat",

                    messages=messages
                )

                final_reply = second_response.choices[0].message.content

                print("[Agent] :", final_reply)

                messages.append(
                    {
                        "role": "assistant",
                        "content": final_reply
                    }
                )


            else:
                # we will directly print LLM's "text" response here
                final_response = response.choices[0].message.content
                print("[Agent] :", final_response)
                messages.append(
                    {
                        "role": "assistant",
                        "content": final_response
                    }
                )


asyncio.run(main())