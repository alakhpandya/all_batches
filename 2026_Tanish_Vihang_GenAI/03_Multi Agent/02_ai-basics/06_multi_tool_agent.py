from openai import OpenAI
import os
from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(
#         base_url="https://openrouter.ai/api/v1",
#         api_key=os.getenv("OPENROUTER_API_KEY")
#     )


# -------------------- Tools --------------------

# Calculator tool
def calculator(expression):
    # expression: "20 + 30"
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# print(calculator("evaluate: 30 - 10"))

# Summarizer tool
def summarize_text(text):
    words = text.split()

    summary = " ".join(words[:20])

    return summary


# Word Counter tool
def count_words(text):
    words = text.split()

    return f"Word count: {len(words)}"


# -------------------- Tool definitions --------------------

tools = [
    {
        "type" : "function",

        "function" : {
            "name" : "calculator",

            "description" : "Perform mathematical operations",

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

    {
        "type" : "function",

        "function" : {
            "name" : "summarize_text",

            "description" : "Summarize long text into short form.",

            "parameters" : {

                "type" : "object",

                "properties" : {

                    "text" : {

                        "type" : "string",

                        "description" : "Text to summarize"

                    }

                },

                "required" : ["text"]
            }
        }
    },

    {
        "type" : "function",

        "function" : {
            "name" : "count_words",

            "description" : "Count total number of words in the text",

            "parameters" : {

                "type" : "object",

                "properties" : {

                    "text" : {

                        "type" : "string",

                        "description" : "Text for word counting"

                    }

                },

                "required" : ["text"]
            }
        }
    }

]


# -------------------- Memory --------------------
