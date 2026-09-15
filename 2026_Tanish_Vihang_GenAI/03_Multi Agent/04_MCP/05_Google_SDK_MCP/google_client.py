from google import genai
from mcp import stdio_client
from mcp import ClientSession
import asyncio


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

from mcp import StdioServerParameters

server_params = StdioServerParameters(
    command= "python",
    args= ["server.py"]
)

from google.genai import types

def convert_mcp_tools(tools_list):
    gemini_tools = []
    for tool in tools_list:
        gemini_tools.append(
            types.FunctionDeclaration(
          
                name= tool.name,

                description= tool.description,

                parameters= tool.inputSchema

            )
        )

    gemini_tools = [types.Tool(
        function_declarations= gemini_tools
    )]
    return gemini_tools


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

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_list = await session.list_tools()

            gemini_tools = convert_mcp_tools(tools_list.tools)
            print("\nTools converted to google's SDK successfully...")

            # --------- LLM Call ----------
            model_id = "gemini-3.5-flash-lite"
            
            response = gemini_client.models.generate_content(

                model= model_id,

                contents= user_prompt,

                config= types.GenerateContentConfig(
                    tools= gemini_tools,
                    temperature= 0.0,
                    max_output_tokens= 500
                )
            )

            print("\nLLM call done...")

            # print("\nLLM Response:\n", response, end="\n\n")

            if response.function_calls:

                chat = gemini_client.chats.create(
                    model= model_id
                )
                chat.send_message(
                    message= user_prompt
                )

                for function_call in response.function_calls:

                    tool_name = function_call.name

                    tool_args = function_call.args

                    print(f"\nCalling Tool: {tool_name}\nArguments: {tool_args}")

                    mcp_result = await session.call_tool(
                        name= tool_name,
                        arguments= tool_args
                    )

                    tool_output = mcp_result.content[0].text
                    print("\nTool Output:", tool_output)

                    final_response = chat.send_message(
                        types.Part.from_function_response(
                            name= tool_name,
                            response= {
                                "result" : tool_output
                            }
                        )
                    )

                    print("\nFinal Response:\n", final_response.text)
            else:
                print("[Agent]:", response.text)

if __name__ == "__main__":
    asyncio.run(main())