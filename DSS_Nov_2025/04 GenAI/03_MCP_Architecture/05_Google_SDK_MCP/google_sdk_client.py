from google import genai
import asyncio
from mcp import StdioServerParameters
from mcp import stdio_client
from mcp import ClientSession
import json


gemini_client = genai.Client()      # It automatically reads the GEMINI_API_KEY environment variable
print("Gemini client created successfully...")

# OR for custom api key:
"""
from dotenv import load_dotenv
import os

load_dotenv()
gemini_client = genai.client(
    api_key = os.getenv("YOUR_ENV_VAR_NAME")
)
"""

server_params = StdioServerParameters(
    command= "python",
    args= ["mcp_server.py"]
)


from google.genai import types

def convert_mcp_tools(mcp_tools):
    gemini_functions = []

    for tool in mcp_tools.tools:

        gemini_functions.append(
            types.FunctionDeclaration(

                name = tool.name,

                description= tool.description,

                parameters= tool.inputSchema

            )
        )

    gemini_tools = [types.Tool(
        function_declarations= gemini_functions
    )]

    return gemini_tools

async def main():
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            mcp_tools = await session.list_tools()

            print("Tools found:")
            i = 1
            for tool in mcp_tools.tools:
                print(f"Tool-{i}:", tool.name)
                i += 1

            gemini_tools = convert_mcp_tools(mcp_tools)
            print("Tools converted in the gemini compatible format...")

            messages = [
                {
                    "role" : "system",

                    "content" : "You are an AI assistant. Strictly use tools whenever available & needed."
                }
            ]

            # user_prompt = "I have 200 USD, how many Euros will it make?"
            # user_prompt = "What is an mcp server? Explain me under 100 words."
            user_prompt = input("[You] : ")
            print("[User] :", user_prompt)


            # --------------- LLM Call ---------------

            # model_id = "gemini-2.5-flash"
            model_id = "gemini-3.5-flash-lite"

            response = gemini_client.models.generate_content(

                model = model_id,

                contents = user_prompt,

                config = types.GenerateContentConfig(
                    tools = gemini_tools,
                    temperature = 0.0
                )
            )

            print("LLM call done successfully...")
            # print("LLM Response:\n", response)

            if response.function_calls:

                chat = gemini_client.chats.create(
                    model = model_id
                )

                chat.send_message(
                    user_prompt
                )

                for function_call in response.function_calls:

                    tool_name = function_call.name

                    tool_args = function_call.args

                    print(f"Calling tool: {tool_name}\nArguments: {tool_args}")

                    mcp_result = await session.call_tool(
                        name = tool_name,

                        arguments = tool_args
                    )

                    tool_output = mcp_result.content[0].text
                    print("Tool output:\n", tool_output)

                    final_response = chat.send_message(
                        types.Part.from_function_response(
                            name = tool_name,
                            response = {
                                "result" : tool_output
                            }
                        )
                    )

                    # print("[Agent] :", final_response)
                    # print("[Agent] :", final_response.candidates[0].content.parts[0].text)
                    print("[Agent] :", final_response.text)

            else:

                print("[Agent] :", response.text)

if __name__ == "__main__":
    asyncio.run(main())