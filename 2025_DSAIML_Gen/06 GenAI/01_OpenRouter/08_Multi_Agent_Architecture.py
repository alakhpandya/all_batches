from dotenv import load_dotenv
from crewai import LLM, Agent, Task
import os

# ---------------------------- LLMs ----------------------------

load_dotenv()
general_llm = LLM(

    base_url= "https://openrouter.ai/api/v1",

    api_key= "os.getenv("OPENROUTER_API_KEY")",
    
    model= "openrouter/free"

    # max_tokens= 200,

    # temperature= 1.2

)

nemotron_llm = LLM(

    base_url= "https://openrouter.ai/api/v1",

    api_key= "os.getenv("OPENROUTER_API_KEY")",
    
    model= "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"

)

# ---------------------------- Agents ----------------------------

researcher_agent = Agent(

    role = "AI Researcher",

    goal = "Find out trending topics related to AI that can go viral",

    backstory = """
    You are an expert researcher who is working at a highly popular AI blogging company that has more than 1 million followers since last 5 years.

    You research & find out hot topics around artificial intelligence, machine learning, robotics, generative AI etc. which are currently getting viral on social media platforms and returns a detailed research report about top-3 topics in the descending order of their chances of getting viral.
    """,

    llm = nemotron_llm,

    verbose = True
)

writer_agent = Agent(
    
    role = "AI blog writer",

    goal = "Write simple & engangging blog articles on the topics provided with their research summary report",

    backstory = """
    You are a senior content writer at a leading blog company and you are an expert when it comes to writing beginner-friendly blog articles which are highly engagging and have very high probablity to go viral on all the social media platforms.
    """,

    llm = general_llm,

    verbose = True

)

reviewer_agent = Agent(

    role = "Content reviewer",

    goal = "Improve the quality and readability of the given blog articles",

    backstory = """
    You are a senior content reviewer in the team of a highly popular blogger. You have expertise in reviewing, improving & editing the provided blog articles.

    You improve grammar, structure, readability & overall quality of the blog articles eventually to further improve their probability of getting viral.
    """,

    llm = general_llm,

    verbose = True

)

# ---------------------------- Tasks ----------------------------
