from crewai import Agent, Task, Crew, LLM, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os 

load_dotenv()

# LLM
llm = LLM(

    model="openrouter/deepseek/deepseek-chat",

    api_key=os.getenv("OPENAI_API_KEY"),

    base_url="https://openrouter.ai/api/v1",

    max_tokens=300,

    temperature=0.7
)

# ---------------- Tools -----------------
search_tool = SerperDevTool()

# Agents
researcher = Agent(

    role="AI Research Specialist",

    goal="""
    Find accurate & useful information about latest Artificial Intelligence trends.
    """,

    backstory="""
    You are an expert AI reseacher.
    You explain concepts clearly and accurately.
    """,

    tools=[search_tool],

    llm=llm,

    verbose=True
)

writer = Agent(

    role="Technical content Writer",

    goal="Write engaging and beginner friendly articles.",

    backstory="""
    You are a professional tech blogger.
    You simplify complex concepts.
    """,

    llm = llm,

    verbose=True
)


# Tasks

research_task = Task(

    description="""
    Research latest Artificial Intelligence trends in 2026.
    Focus on:
    - AI agents
    - Generative AI
    - Automation
    - Business applications
    - AI coding assistants
    """,

    expected_output="A clear research summary about Generative AI trends.",

    agent=researcher
)

writing_task = Task(

    description="""
    Write beginner friendly blog articles using the research summary.
    Make it easy to understand and engaging.
    """,

    expected_output="A complete blog article.",

    agent=writer
)


# Crew
crew = Crew(

    agents=[researcher, writer],

    tasks=[research_task, writing_task],

    process = Process.sequential,

    verbose=True
)

# Run
result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)