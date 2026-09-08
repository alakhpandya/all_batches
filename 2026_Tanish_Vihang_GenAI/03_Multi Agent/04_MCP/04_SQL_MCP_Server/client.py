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

MODEL = os.getenv("OPENAI_MODEL_NAME")    # model name in my system env var (first priority)
# MODEL = os.getenv("NEMOTRON_REASONING_FREE")    # model name in my system env var (first priority)
# MODEL = os.getenv("MODEL_NAME")    # model name var from my .env file
# print("Model:", MODEL)


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

    server_params = StdioServerParameters(

        command= "python",

        args= ["sql_server.py"]

    )

    async with stdio_client(server_params) as (

        read_stream,

        write_stream

    ):

        async with ClientSession(

            read_stream,

            write_stream

        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            openai_tools = convert_mcp_tools(tools.tools)

            print("Type 'exit' whenever you want to quit...")

            while True:

                question = input("\nAsk something to your SQL Assistant:\n")

                if question.lower() == "exit":

                    break

                messages = [
                    {

                        "role" : "user",

                        "content" : question

                    }
                ]

                while True:
                    response = client.chat.completions.create(

                        messages= messages,

                        model= MODEL,

                        tools= openai_tools,

                        tool_choice= "auto"

                    )

                    assistant = response.choices[0].message
                    # print("\nResponse:")
                    # print(assistant, "\n")

                    if assistant.reasoning:
                        print(f"Thinking:\n{assistant.reasoning}")

                    if not assistant.tool_calls:

                        print("Answer:\n")

                        print(assistant.content)

                        messages.append({
                            "role" : "assistant",
                            "content" : assistant.content
                        })

                        break

                    messages.append(assistant)

                    for tool_call in assistant.tool_calls:

                        tool_name = tool_call.function.name

                        arguments = json.loads(

                            tool_call.function.arguments

                        )

                        print("\nCalling tool:", tool_name)

                        print(f"\nArguments:\n{arguments}\n")

                        result = await session.call_tool(

                            name= tool_name,

                            arguments= arguments

                        )

                        messages.append({

                            "role" : "tool",

                            "tool_call_id" : tool_call.id,

                            "content" : str(result)

                        })


if __name__ == "__main__":
    asyncio.run(main())