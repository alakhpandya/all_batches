from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os 

load_dotenv()

# Creating OpenRouter LLM
llm = LLM(

    # model="openrouter/google/gemma-3-27b-it:free",
    model="openrouter/deepseek/deepseek-chat",

    api_key=os.getenv("OPENAI_API_KEY"),

    base_url="https://openrouter.ai/api/v1",

    max_tokens=100,

    temperature=0.7
)


researcher = Agent(

    role="AI Researcher",

    goal="Explain Artificial Intelligence simply.",

    backstory="""
    You are an expert AI teacher.
    Explain concepts in beginner-friendly language.
    """,

    llm=llm,

    verbose=True
)

task = Task(

    description="""
    Explain Generative AI in simple language
    with real-world examples.
    """,

    expected_output="Simple beginner-friendly explanation.",

    agent=researcher
)

writer = Agent(

    role="AI Writer",

    goal="Write simple and engaging AI articles.",

    backstory="""
    You are a professional tech writer.
    You create beginner-friendly content.
    """,
    llm = llm,

    verbose=True
)

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

# crew = Crew(

#     agents=[researcher],

#     tasks=[task],

#     verbose=True
# )


crew = Crew(

    agents=[researcher, writer],

    tasks=[research_task, writing_task],

    verbose=True
)

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)