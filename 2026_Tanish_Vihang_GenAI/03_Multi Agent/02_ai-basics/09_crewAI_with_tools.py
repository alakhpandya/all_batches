from crewai import Task, Agent, Crew, Process, LLM
from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool 

load_dotenv()

# Creating OpenRouter LLM
llm = LLM(
    model= "openrouter/deepseek/deepseek-chat",

    api_key= os.getenv("OPENROUTER_API_KEY"), 

    base_url= "https://openrouter.ai/api/v1",

    max_tokens= 100,

    temperature= 0.7
)


# ---------------- Tools ----------------

search_tool = SerperDevTool()

# ---------------- AGENTS ----------------

researcher = Agent(

    role="AI Researcher",

    goal="Find useful information about Artificial Intelligence and explain them simply.",

    backstory="""
    You are an expert AI researcher.
    You explain concepts clearly and in a beginner-friendly language.
    """,

    tools= [search_tool],

    verbose=True,

    llm=llm
)

writer = Agent(

    role="AI Writer",

    goal="Write simple and engaging AI articles.",

    backstory="""
    You are a professional tech writer.
    You create beginner-friendly content.
    """,

    verbose=True,

    llm=llm
)

# ---------------- TASKS ----------------

research_task = Task(

    description="""
    Research Artificial Intelligence trends in 2026.
    Focus on:
    - AI agents
    - Generative AI
    - Automation
    """,

    expected_output="A detailed research summary.",

    agent=researcher
)

writing_task = Task(

    description="""
    Write a beginner-friendly blog article
    based on the research provided.
    """,

    expected_output="A simple blog article.",

    agent=writer
)

# ---------------- CREW ----------------

crew = Crew(

    agents= [researcher, writer],

    tasks= [research_task, writing_task],

    process= Process.sequential,

    verbose= True
)

# ---------------- RUN CREW ----------------

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)