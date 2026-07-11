from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ---------------- TOOLS ---------------- 

# Calculator Tool
def calculator(expression):

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error: {str(e)}"

 
# Summarizer Tool
def summarize_text(text):

    words = text.split()

    summary = " ".join(words[:20])

    return f"Summary: {summary}..."


# Word Counter Tool
def count_words(text):

    words = text.split()

    return f"Word Count: {len(words)}"


# ---------------- TOOL DEFINITIONS ---------------- 

tools = [

    {
        "type": "function",

        "function": {

            "name": "calculator",

            "description": "Perform mathematical calculations.",

            "parameters": {

                "type": "object",

                "properties": {

                    "expression": {

                        "type": "string",

                        "description": "Mathematical expression"
                    }
                },

                "required": ["expression"]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "summarize_text",

            "description": "Summarize long text into short form.",

            "parameters": {

                "type": "object",

                "properties": {

                    "text": {

                        "type": "string",

                        "description": "Text to summarize"
                    }
                },

                "required": ["text"]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "count_words",

            "description": "Count total words in text.",

            "parameters": {

                "type": "object",

                "properties": {

                    "text": {

                        "type": "string",

                        "description": "Text for word counting"
                    }
                },

                "required": ["text"]
            }
        }
    }
]

# ---------------- MEMORY ---------------- 

messages = [

    {
        "role": "system",
        "content": """
        You are an intelligent AI assistant.

        Use tools whenever needed.

        Available capabilities:
        - math calculations
        - text summarization
        - word counting
        """
    }
]

print("Multi-Tool AI Agent Started!")
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

        tools=tools,

        tool_choice="auto"
    )

    response_message = response.choices[0].message

    # TOOL EXECUTION
    if response_message.tool_calls:

        tool_call = response_message.tool_calls[0]
        # print("response_message.tool_calls:", response_message.tool_calls)

        function_name = tool_call.function.name

        arguments = json.loads(tool_call.function.arguments)

        # Calculator Tool
        if function_name == "calculator":

            result = calculator(arguments["expression"])

        # Summarizer Tool
        elif function_name == "summarize_text":

            result = summarize_text(arguments["text"])

        # Word Counter Tool
        elif function_name == "count_words":

            result = count_words(arguments["text"])

        else:

            result = "Unknown Tool"

        print(f"Tool Used: {function_name}")
        print("Tool Result:", result)

        # Store assistant tool request
        messages.append(response_message)

        # Store tool output
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            }
        )

        # SECOND API CALL
        second_response = client.chat.completions.create(

            model="deepseek/deepseek-chat",

            messages=messages
        )

        final_reply = second_response.choices[0].message.content

        print("AI:", final_reply)

        messages.append(
            {
                "role": "assistant",
                "content": final_reply
            }
        )

    else:

        ai_reply = response_message.content

        print("AI:", ai_reply)

        messages.append(
            {
                "role": "assistant",
                "content": ai_reply
            }
        )

print(messages)