"""
Create an AI recruitment company.

Create agents:
- Resume Analyser
- Skill Evaluator
- HR Reviewer

Workflow:
- Resume Analyzer => Skill Evaluator => HR Reviewer

User will provide:
- Text of the resume of the candidate

AI System will do:
- Evaluate skills
- Evaluate candidate also
- Identify strengths and weaknesses
- Generate hiring recommendation

Rubric:

**Concepts to be implimented**
1. Multi-stage AI evaluation pipeline
	- Flow: Raw Resume => Analysis => Skill Evaluation => HR Decision

2. "Division of Labor" / Specialized Agents
Make each agent:
	- having responsiblity as narrow as possible
	- focussed deeply
	- improves workflow quality

3. Sequential Context Sharing
	- Use CrewAI to automatically pass extracted information, evaluation context and previous outputs between agents

4. Business AI Systems/AI workflow automation

**Testing of your workflow**

Observe the final output (Rejection/Acceptance) by the system by providing:
- weak resume with fewer skills and no projects
- resumes for different job roles like Data Scientist, Frontend Developer, AI Engineer, Data Analysts etc


**Upgrade**

- Add ATS scoring agent that checks ATS Compatibility
- Add an Interview Question Generator agent for technical round based on the resume


**Importance of AI Supervision**

- Figure out and make a note of the limitations of your AI Systems.

"""

from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# LLM

llm = LLM(

    model="openrouter/deepseek/deepseek-chat",

    api_key=os.getenv("OPENAI_API_KEY"),

    base_url="https://openrouter.ai/api/v1",

    max_tokens=300,

    temperature=0.7
)

# SAMPLE RESUME

resume_text = """

Rajeev Dey

Skills:
Python, SQL, Machine Learning, Tableau,
Excel, Deep Learning, Generative AI

Experience:
Built ML projects using Scikit-learn and TensorFlow.
Created AI chatbot using OpenRouter API.

Education:
B.Tech in Computer Engineering
"""

# AGENTS

resume_analyzer = Agent(

    role="Resume Analyzer",

    goal="""
    Analyze candidate resume carefully.
    Extract important information.
    """,

    backstory="""
    You are an expert resume screening specialist.
    You identify candidate strengths and experience.
    """,

    llm=llm,

    verbose=True
)

skill_evaluator = Agent(

    role="Skill Evaluator",

    goal="""
    Evaluate technical skills and job readiness.
    """,

    backstory="""
    You are a senior technical interviewer.
    You evaluate candidate skills professionally.
    """,

    llm=llm,

    verbose=True
)

hr_reviewer = Agent(

    role="HR Reviewer",

    goal="""
    Decide whether candidate should be shortlisted.
    """,

    backstory="""
    You are an experienced HR manager.
    You make final hiring recommendations.
    """,

    llm=llm,

    verbose=True
)

# TASKS

analysis_task = Task(

    description=f"""
    Analyze this resume carefully:

    {resume_text}

    Extract:
    - skills
    - education
    - projects
    - experience
    """,

    expected_output="""
    Structured resume analysis.
    """,

    agent=resume_analyzer
)

evaluation_task = Task(

    description="""
    Evaluate candidate's technical capabilities.

    Check:
    - AI knowledge
    - programming skills
    - project experience
    - industry readiness
    """,

    expected_output="""
    Technical evaluation report.
    """,

    agent=skill_evaluator
)

hr_task = Task(

    description="""
    Review candidate profile and provide:

    - strengths
    - weaknesses
    - hiring recommendation
    - suggested job role
    """,

    expected_output="""
    Final HR hiring report.
    """,

    agent=hr_reviewer
)

# CREW

crew = Crew(

    agents=[
        resume_analyzer,
        skill_evaluator,
        hr_reviewer
    ],

    tasks=[
        analysis_task,
        evaluation_task,
        hr_task
    ],

    process=Process.sequential,

    verbose=True
)

# Kick Off

result = crew.kickoff()

print("\nFINAL HR REPORT:\n")
print(result)