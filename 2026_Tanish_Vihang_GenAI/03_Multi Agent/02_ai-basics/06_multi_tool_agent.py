from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )


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
messages = [

    {
        "role": "system",
        "content": """
        You are an intelligent AI assistant.

        Use tools whenever needed.

        Available capabilities:
        - math calculation
        - text summarization
        - word count
        """
    }

]

print("Mullit-tool agent started!!")
print("Type 'exit' to quit")

# -------------------- Chat loop --------------------
while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role" : "user",
        "content" : user_input
    })

    # First API Call
    response = client.chat.completions.create(
        model = "deepseek/deepseek-chat",
        messages= messages,
        tools= tools,
        tool_choice= "auto"
    )

    # user_input = "I have $100 in my wallet, if my cousine takes out $30, what will I left with?"
    # print(response)
    """
    ChatCompletion(id='gen-1782870339-LCjKlEOCL1N62nOpKL3q', 
    choices=[Choice(finish_reason='tool_calls', 
        index=0, 
        logprobs=None, 
        message=ChatCompletionMessage(
            content=None, 
            refusal=None, 
            role='assistant', 
            annotations=None, 
            audio=None, 
            function_call=None, 
            tool_calls=[ChatCompletionMessageFunctionToolCall(id='a78f9e8e33454fc495d40a51efb481e3', 
                function=Function(arguments='{"expression":"100 - 30"}', name='calculator'), 
                type='function', index=0)], 
                reasoning=None
            ), 
        native_finish_reason='tool_calls')
    ], 
    created=1782870339, 
    model='deepseek/deepseek-chat-v3', 
    object='chat.completion', 
    moderation=None, 
    service_tier=None, 
    system_fingerprint=None, 
    usage=CompletionUsage(completion_tokens=43, prompt_tokens=643, total_tokens=686, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=None, image_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0, cache_write_tokens=0, video_tokens=0), cost=0.0001631329, is_byok=False, cost_details={'upstream_inference_cost': 0.0001631329, 'upstream_inference_prompt_cost': 0.0001287286, 'upstream_inference_completions_cost': 3.44043e-05}), provider='StreamLake')
    """
    # user_input = "I want to use AI agents to boost my productivity, give me 3 ideas under 100 words."
    # print(response)
    """
    ChatCompletion(id='gen-1782871062-2YgxXx7A3uOiK7aCzun7', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="Here are three concise ideas (each under 100 words) to use AI agents for boosting productivity:  \n\n1. **Automate Repetitive Tasks**: Use AI agents to handle routine tasks like scheduling meetings, sorting emails, or data entry. This frees up time for more strategic work.  \n\n2. **Smart Note-Taking**: Deploy AI to transcribe and summarize meetings or lectures in real-time, highlighting key points and action items for quick review.  \n\n3. **Personalized Learning Assistant**: Leverage AI to curate and summarize articles, research papers, or reports tailored to your interests, helping you stay updated without information overload.  \n\nLet me know if you'd like me to expand on any of these!", refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning=None), native_finish_reason='stop')], created=1782871062, model='deepseek/deepseek-chat-v3', object='chat.completion', moderation=None, service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=146, prompt_tokens=640, total_tokens=786, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=None, image_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0, cache_write_tokens=0, video_tokens=0), cost=0.0002449426, is_byok=False, cost_details={'upstream_inference_cost': 0.0002449426, 'upstream_inference_prompt_cost': 0.000128128, 'upstream_inference_completions_cost': 0.0001168146}), provider='StreamLake')
    """


    response_message = response.choices[0].message

    if response_message.tool_calls:
        tool_call = response_message.tool_calls[0]

        function_name = tool_call.function.name

        arguments = json.loads(tool_call.function.arguments)

        # Calculator tool call:
        if function_name == "calculator":
            result = calculator(arguments["expression"])
        
        # Summarizer tool call:
        elif function_name == "summarize_text":
            result = summarize_text(arguments["text"])
        
        # Word count tool call:
        elif function_name == "count_words":
            result = count_words(arguments["text"])

        else:
            result = "Unknown Tools"

        print("Tool used:", function_name)
        print("Tool output:", result)
        
        # Store the tool call request
        messages.append(response_message)

        # Store tool output
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

        # Second API call
        second_response = client.chat.completions.create(

            model="deepseek/deepseek-chat",

            messages=messages
        )

        final_reply = second_response.choices[0].message.content

        print("Agent:", final_reply)

        messages.append({
            "role" : "assistant",
            "content" : final_reply
        })

    else:
        ai_reply = response_message.content

        print("Agent:", ai_reply)

        messages.append({
            "role" : "assistant",
            "content" : ai_reply
        })


print(messages)