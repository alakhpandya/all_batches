from crewai import Agent
from crewai import Task
from crewai import Crew

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ---------------- AGENTS ----------------

researcher = Agent(

    role="AI Researcher",

    goal="Find useful information about Artificial Intelligence.",

    backstory="""
    You are an expert AI researcher.
    You explain concepts clearly.
    """,

    verbose=True
)

writer = Agent(

    role="AI Writer",

    goal="Write simple and engaging AI articles.",

    backstory="""
    You are a professional tech writer.
    You create beginner-friendly content.
    """,

    verbose=True
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

    agents=[researcher, writer],

    tasks=[research_task, writing_task],

    verbose=True
)

# ---------------- RUN CREW ----------------

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)