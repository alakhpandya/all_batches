from crewai import Agent
from crewai import Task
from crewai import Crew
from crewai import Process

from dotenv import load_dotenv
import os

load_dotenv()

# ---------------- AGENTS ----------------
researcher = Agent(

    role="AI Researcher",

    goal="Find useful information about Artificial Intelligence.",

    backstory="""
    You are an expert AI researcher.
    You explain concepts clearly.
    """,

    verbose=False
)

writer = Agent(

    role="AI Writer",

    goal="Write simple and engaging AI articles.",

    backstory="""
    You are a professional tech writer.
    You create beginner-friendly content.
    """,

    verbose=False
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

    verbose= False
)

# ---------------- RUN CREW ----------------

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)