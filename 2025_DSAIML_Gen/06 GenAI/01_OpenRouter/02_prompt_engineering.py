from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
agent = OpenAI(

    base_url="https://openrouter.ai/api/v1",
    
    api_key=os.getenv("OPENROUTER_API_KEY")

)


# ------------------------- "role" : "system" -------------------------

"""
response = agent.chat.completions.create(
    
        # model="google/gemma-4-31b-it:free",
        # model="deepseek/deepseek-v4.1-flash",
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
    
        messages=[
            {
                "role" : "system",

                "content" : "You are a teacher who teaches computers to grade-5 students."
            },
            {
                "role" : "user",

                "content" : "Explain me what is data science under 200 words."
            }
        ]

    )

# print("Response:", response.choices[0].message.content)
"""

# print("Royal AI Agent is ready to help you!\nWhat can I help you with today?\n")
# prompt = input("[You] : ")
prompt = "None"

messages=[
    {
        "role" : "system",

        # "content" : "You are a teacher who teaches computers to grade-5 students."
        "content" : "You are an experienced software engineer with 10 years of industry experience."
    },
    {
        "role" : "user",

        # "content" : "Explain me what is data science under 200 words."
        "content" : prompt
    }
]

# ------------------------- Few shot prompting -------------------------

messages = [
    {
        "role" : "system",

        "content" : "You are a sentiment analyst AI"
    },
    {
        "role" : "user",

        "content" : "I loved that movie!"
    },
    {
        "role" : "assistant",

        "content" : "Positive"
    },
    {
        "role" : "user",

        "content" : "The food at this restaurant is terrible."
    },
    {
        "role" : "assistant",

        "content" : "Negative"
    },
        {
        "role" : "user",

        "content" : "The play at the theatre was ok"
    },
    {
        "role" : "assistant",

        "content" : "Neutral"
    },
    {
        "role" : "user",

        "content" : prompt
    }
]

# --------------------- Generating Structured Output ---------------------

messages=[
    {
        "role" : "user",

        "content" : """
            Give me the output in jSon format:

            name
            age
            gender

            Student: Aniket, 21, Male
            """
    }
]

# --------------------- Multi-turn Conversation/Conversation Memory ---------------------

messages = [
    {
        "role" : "user",

        "content" : "Hi, Dev this side."
    },
    {
        "role" : "assistant",

        "content" : "He Dev, how may I help you today?"
    },
    {
        "role" : "user",

        "content" : "I want to write a note on different concepts of Generative AI (each topic not more than 50 words). Here is the first topic: The difference between an AI agent & an LLM"
    },
    {
        "role" : "assistant",

        "content" : "Think LLM as a brain and an AI agent as a complete body with brain"
    },
    {
        "role" : "user",

        "content" : prompt
    }
]

# response = agent.chat.completions.create(

#     model="nvidia/nemotron-3-ultra-550b-a55b:free",

#     messages= messages

# )


# --------------------- Hyperparameter "temperature" ---------------------
"""
The temperature parameter in the OpenAI SDK ranges from 0.0 to 2.0, with a default value of 1.0.

How Temperature Works

• 0.0 to 0.3 (Low): Makes the output more focused, deterministic, and consistent (best for coding, math, or data extraction).
• 0.7 to 1.0 (Moderate): Balances coherence and creativity (standard for general conversation and writing).
• 1.0 to 2.0 (High): Increases randomness, diversity, and "poetic" or unexpected word choices (best for brainstorming or creative writing).

Best Practices

• Change one at a time: The OpenAI Community Forum features a consensus advising developers to adjust either temperature or top_p, but not both at the same time.
• Over 1.0: Values above 1.0 can cause the model's output to degrade or hallucinate more quickly, so test changes incrementally.
"""

'''
# user_prompt = input("[You] : ")
user_prompt = "Write a 100 words story on this plot: I was walking down the street that night..."

messages = [
    {
        "role" : "system",

        "content" : "You are a story teller who creates short stories in simple & easy English."
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]


response = agent.chat.completions.create(

    model="nvidia/nemotron-3-ultra-550b-a55b:free",

    messages= messages,

    # temperature= 0.1
    temperature= 1.9
)

print("[Agent] :", response.choices[0].message.content)
'''

# --------------------- Hyperparameter "max_tokens" ---------------------
user_prompt = "What is agentic AI?"
messages = [
    {
        "role" : "system",

        "content" : "You are a data scientist with 5 years of experience in companies like Microsoft, IBM, NVidea etc"
    },
    {
        "role" : "user",

        "content" : user_prompt
    }
]


response = agent.chat.completions.create(

    model="nvidia/nemotron-3-ultra-550b-a55b:free",

    messages= messages,

    # max_tokens= 100
    max_completion_tokens= 100
)

print("[Agent] :", response.choices[0].message.content)