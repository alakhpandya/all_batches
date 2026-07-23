from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

# ----------------- LLM -----------------
llm = LLM(

    model = "openrouter/deepseek/deepseek-chat",

    api_key= os.getenv("OPENROUTER_API_KEY"),

    base_url= "https://openrouter.ai/api/v1",

    # max_tokens=200,

    temperature=0.7
)


# ----------------- Tools -----------------

search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()

# ----------------- Agents -----------------

researcher = Agent(
    
    role = "News Researcher",

    goal = "Find out trending news and current affairs which are getting popular in present time by searching on google",

    backstory = """
    You are an expert researcher who is working for a leading blogging company since 5 years.
    
    You search & find out the hot topics on Geopolitics, Finance, Stock markets etc. internationally as well as in India that are currently getting viral on social media platforms and return a list of such 3 topics in the descending order of their probability of going viral.
    """,

    verbose = True,

    llm= llm,

    tools = [search_tool, scraper_tool]
)

writer = Agent(
    
    role = "Blog Writer",

    goal = "Write simple & engaging short articles on the provided hot topics",

    backstory = """
    You are a senior writer who has expertise in writing viral blog articles for a leading blogging company since 5 years.
    
    You write beginner-friendly and engaging content that readers on the social media platforms like. 
    """,

    verbose = True, 

    llm= llm
)

reviewer = Agent(
    
    role = "Content reviewer",

    goal = "Improve blog's quality and readability",

    backstory = """
    You are a senior content reviewer who has expertise in reviewing, improving and editing blog articles for a leading blogging company since 5 years.
    
    You improve grammar, structure & quality of the articles to make them more engaging and more viral.
    """,

    verbose = True,

    llm= llm
)

# ----------------- Tasks -----------------

research_task = Task(
    
    description="""
    Research latest current affairs which are trending in present time.
    Focus in these areas:
    - International Geopolitical News
    - Indian domestic political news
    - Indian weather updates
    - World economics & stock market updates
    - Indian stock market news, latest gold prices etc.
    """,

    expected_output= "A clear research summary with a list of top 3 trending topics",

    agent= researcher
)

writing_task = Task(
    
    description="""
    Write beginner-friendly short blog articles based on research summary.
    Make it easy to understand and engaging.
    """,

    expected_output= "A complete blog article",

    agent= writer
)

review_task = Task(
    
    description="""
    Review and improve the blog article.

    Fix:
    - grammar
    - readablity
    - clarity
    - structure
    """,

    expected_output= "Final polished blog article.",

    agent= reviewer
)

# ----------------- Crew -----------------

crew = Crew(

    agents= [researcher, writer, reviewer],

    tasks= [research_task, writing_task, review_task],

    process= Process.sequential,

    verbose= True

)

# ----------------- Starting the Crew -----------------

result = crew.kickoff()

print("\n\n:::Final Result:::\n")
print(result)