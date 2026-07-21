from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

agent = OpenAI(
    
    base_url="https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)


# ----------------------- Tools -----------------------

# Calculator tool
# expression = input("[You]: ")
# print("Answer =", eval(expression))

def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"
    
# print("Result =", calculator(expression))

# Text summarizer tool
def summarizer(text):
    word_list = text.split()
    summary_list = word_list[ :20]
    summary =  " ".join(summary_list)
    return summary


# Word counting tool
def count_words(text):
    word_list = text.split()

    return f"Word count: {len(word_list)}"


# -------------------- Tool definitions (as per OpenAI's SDK) --------------------

tools = [
    # Tool-1
    {
        "type" : "function",

        "function" : {

            "name" : "calculator",

            "description" : "Performs mathematical operations on given expression",

            "parameters" : {

                "type" : "object",

                "properties" : {

                    "expression" : {

                        "type" : "string",

                        "description" : "Mathematical expression"

                    }

                },

                "required" : ["expression"]
            }

        }
    },
    # Tool-2
    {
        "type" : "function",

        "function" : {

            "name" : "summarizer",

            "description" : "Gives the summary of the text provided",

            "parameters" : {

                "type" : "object",

                "properties" : {

                    "text" : {

                        "type" : "string",

                        "description" : "Text to be summarized"

                    }

                },

                "required" : ["text"]
            }

        }
    },
    # Tool-3
    {
        "type" : "function",

        "function" : {

            "name" : "count_words",

            "description" : "Counts the words of the given text",

            "parameters" : {

                "type" : "object",

                "properties" : {

                    "text" : {

                        "type" : "string",

                        "description" : "Text to count words"

                    }

                },

                "required" : ["text"]
            }

        }
    }
]

# print(tools)
# from pprint import pprint

# pprint(tools)

# -------------------- Memory --------------------
messages = [
    {
        "role" : "system",

        "content" : """
        You are an intelligent AI assistant.

        Stictly use tools whenever needed. Don't perform task by your own if there is a tool available to do it.

        Available capabilities:
        - Mathematical calculations
        - Text summarization
        - Counting words in given text
        """
    }
]


welcome_msg = ("-" * 50) + (" Multi tool agent started ") + ("-" * 50)
print(welcome_msg.center(150))

print('\nAsk me for any help related to your health or type "exit" to end the conversation.\n')

while True:
    user_prompt = input("\n\n[You] : ")

    if user_prompt.lower() == "exit":
        break

    messages.append({
        "role" : "user",

        "content" : user_prompt
    })

    response = agent.chat.completions.create(

        model= "deepseek/deepseek-chat",

        messages= messages,

        tools= tools,

        tool_choice= "auto"

    )

    # ai_response = response.choices[0].message.content
    response = response.choices[0].message

    # print("Response:\n", response)
    if response.tool_calls:
        # print("There is a tool call.")

        # Storing the response (tool call) into conversation memory
        messages.append(response)

        # print(response.tool_calls)
        tool_call = response.tool_calls[0]

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        # print(type(arguments))
        # print(arguments)

        if tool_name == "calculator":
            result = calculator(arguments["expression"])

        elif tool_name == "summarizer":
            result = summarizer(arguments["text"])

        elif tool_name == "count_words":
            result = count_words(arguments["text"])

        else:
            result = "Error: Unknown tool"

        # print("Tool output:", result)

        # Storing tool output into the conversation memory
        messages.append({
            "role" : "tool",

            "tool_call_id" : tool_call.id,

            "content" : result
        })

        # Second API(LLM) Call
        final_response = agent.chat.completions.create(

            model= "deepseek/deepseek-chat",

            messages= messages
        )
        ai_reply = final_response.choices[0].message.content

    else:
        ai_reply = response.content
        
        
    # Storing final ai_reply into conversation memory
    messages.append({
        "role" : "assistant",

        "content" : ai_reply
    })
    print("[Agent]:", ai_reply)