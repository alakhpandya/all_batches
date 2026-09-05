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

    # base_url= os.getenv("OPENAI_API_BASE")      # my system env var name
    
    base_url= os.getenv("OPENAI_BASE_URL")      # from .env file

)

# MODEL = os.getenv("OPENAI_MODEL_NAME")    # model name in my system env var

MODEL = os.getenv("MODEL_NAME")     # model name from .env file

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

            openai_tools = []

            for tool in tools.tools:

                openai_tools.append({

                    "type" : "function",

                    "function" : {

                        "name" : tool.name,

                        "description" : tool.description,

                        "parameters" : tool.inputSchema

                    }

                })

            print('Type "exit" whenever you want to quit...')

            while True:

                question = input("\nAsk something to your SQL Assistant: ")

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

                        model= MODEL,

                        messages= messages,

                        tools= openai_tools,

                        tool_choice= "auto"

                    )

                    assistant = response.choices[0].message

                    if not assistant.tool_calls:

                        print("Answer:\n\n")

                        print(assistant.content)

                        break

                    messages.append(assistant)

                    for tool_call in assistant.tool_calls:

                        tool_name = tool_call.function.name

                        arguments = json.loads(

                            tool_call.function.arguments

                        )

                        print("\nCalling tool:", tool_name)

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