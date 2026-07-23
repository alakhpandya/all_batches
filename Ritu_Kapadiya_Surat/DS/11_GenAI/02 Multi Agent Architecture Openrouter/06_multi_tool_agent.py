from openai import OpenAI
import os
from dotenv import load_dotenv
from pprint import pprint
import json

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
)


# -------------------- Tools --------------------

# Calculator tool

# def calculator(expression):
#     return eval(expression)


def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"
    
# exp = input("What do you want to evaluate?\n")
# ans = calculator(exp)
# print(f"{exp} =", ans)
# print("Thank you for using our software!")

# Summarizer tool
def summarizer(text):
    words = text.split()

    summary_words = words[:20]
    summary = " ".join(summary_words)

    return summary

# Word counting tool
def count_words(text):
    words = text.split()
    return f"Word count: {len(words)}"

# -------------------- Tool definitions (Compatible to OpenAI SDK) --------------------

openai_tools = [
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

                        "description" : "Mathematical Expression"
                    }
                },

                "requiered" : ["expression"]
            }

        }
    },
    # Tool-2
    {
        "type" : "function",

        "function" : {
            
            "name" : "summarizer",
            
            "description" : "Summarizes the text provided",
            
            "parameters" : {

                "type" : "object",

                "properties" : {

                    "text" : {

                        "type" : "string",

                        "description" : "Text to be summarized"
                    }
                },

                "requiered" : ["text"]
            }

        }
    },
    # Tool-3
    {
        "type" : "function",

        "function" : {
            
            "name" : "count_words",
            
            "description" : "Counts and returns number of words present in the text provided",
            
            "parameters" : {

                "type" : "object",

                "properties" : {

                    "text" : {

                        "type" : "string",

                        "description" : "Text to count words"
                    }
                },

                "requiered" : ["text"]
            }

        }
    }
]

# print(openai_tools)
# pprint(openai_tools)

# -------------------- Memory --------------------
messages = [
    {
        "role" : "system",

        "content" : """
        You are an intelligent AI assistant.

        Use tools whenever needed.

        Available capabilities:
        - mathematical calculations
        - text summarization
        - word count
        """
    }
]

print("Multi-tool agent started!")
print("Type 'exit' whenever you want to quit.")

# -------------------- Chat loop --------------------
while True:
    user_prompt = input("\n[You]: ")

    if user_prompt.lower() == "exit":
        break

    messages.append({
        "role" : "user",
        "content" : user_prompt
    })

    # First API Call
    response = client.chat.completions.create(
        model = "deepseek/deepseek-chat",
        messages= messages,
        tools= openai_tools,
        tool_choice= "auto"
    )

    # print("Response:\n", response)
    # print("\nResponse.choices[0]:\n", response.choices[0])
    # print("Response:\n", response.choices[0].message.content)
    response = response.choices[0].message

    if response.tool_calls:
        tool_call = response.tool_calls[0]

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        
        if tool_name == "calculator":
            result = calculator(arguments["expression"])

        elif tool_name == "summarizer":
            result = summarizer(arguments["text"])

        elif tool_name == "count_words":
            result = count_words(arguments["text"])

        else:
            result = "Unknown tool."

        print("Tool name:", tool_name)
        print("Tool output:", result)

        # Store tool call request in the conversation memory
        messages.append(response)

        # Store the tool output in the memory
        messages.append({
            "role" : "tool",
            "tool_call_id" : tool_call.id,
            "content" : str(result)
        })  

        # Second API Call
        second_response = client.chat.completions.create(
            model= "deepseek/deepseek-chat",
            messages= messages
        )

        final_result = second_response.choices[0].message.content

    else:
        final_result = response.choices[0].message.content
        pass

    print("[AI Agent]:", final_result)

    # Store final result into the conversation memory
    messages.append({
        "role" : "assistant",
        "content" : final_result
    })