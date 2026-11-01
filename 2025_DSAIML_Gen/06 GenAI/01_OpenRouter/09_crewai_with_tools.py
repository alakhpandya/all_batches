from dotenv import load_dotenv
from crewai import LLM, Agent, Task, Crew, Process
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# ---------------------------- LLMs ----------------------------

load_dotenv()
general_llm = LLM(

    base_url= "https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY"),
    
    model= "openrouter/free"

    # max_tokens= 200,

    # temperature= 1.2

)

nemotron_llm = LLM(

    base_url= "https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY"),
    
    model= "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"

)

# ---------------------------- Tools ----------------------------
google_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()

# ---------------------------- Agents ----------------------------

researcher_agent = Agent(

    role = "AI Researcher",

    goal = "Find out trending topics related to AI that can go viral",

    backstory = """
    You are an expert researcher who is working at a highly popular AI blogging company that has more than 1 million followers since last 5 years.

    You research & find out hot topics around artificial intelligence, machine learning, robotics, generative AI etc. which are currently getting viral on social media platforms and returns a detailed research report about top-3 topics in the descending order of their chances of getting viral.
    """,

    llm = nemotron_llm,

    verbose = True,

    tools= [google_search_tool, web_scraping_tool]
    
)

writer_agent = Agent(
    
    role = "AI blog writer",

    goal = "Write simple & engangging blog articles on the topics provided with their research summary report",

    backstory = """
    You are a senior content writer at a leading blog company and you are an expert when it comes to writing beginner-friendly blog articles which are highly engagging and have very high probablity to go viral on all the social media platforms.
    """,

    # llm = general_llm,
    llm = nemotron_llm,

    verbose = True

)

reviewer_agent = Agent(

    role = "Content reviewer",

    goal = "Improve the quality and readability of the given blog articles",

    backstory = """
    You are a senior content reviewer in the team of a highly popular blogger. You have expertise in reviewing, improving & editing the provided blog articles.

    You improve grammar, structure, readability & overall quality of the blog articles eventually to further improve their probability of getting viral.
    """,

    # llm = general_llm,
    llm = nemotron_llm,

    verbose = True

)

# ---------------------------- Tasks ----------------------------

research_task = Task(
    description= """
    Research the latest trends in Artificial Intelligence and identify the top 3 most relevant and widely discussed topics based on recent developments, industry adoption, research publications, and community interest. For each topic, prepare a comprehensive research summary that includes an overview, why the topic is currently trending, key concepts, important technologies or tools involved, real-world applications, recent advancements, benefits, challenges, and future outlook. Ensure that the information is accurate, well-structured, objective, and easy to understand. The research summary should provide sufficient depth for another agent to create a high-quality blog article without requiring any additional research.
    """,

    expected_output= "A clear and detailed research summary report of top-3 topics",

    agent= researcher_agent
)

writing_task = Task(

    description= """
    Using the research summary provided by the previous task, write a separate blog article for each of the identified AI topics. Each article should be beginner-friendly, engaging, informative, and concise while maintaining technical accuracy. Use simple language, an attention-grabbing introduction, clear headings and subheadings, short paragraphs, practical examples or analogies where appropriate, and a motivating conclusion. Do not introduce information that is not supported by the provided research summary. The articles should be original, easy to read, and optimized for audience engagement.
    """,

    expected_output= "A complete blog article",

    agent= writer_agent

)

review_task = Task(

    description= """
    Review the blog articles produced by the writing task and improve their overall quality without changing their intended meaning. Correct grammatical, spelling, punctuation, and formatting errors. Enhance sentence clarity, readability, coherence, and logical flow. Improve transitions between sections, eliminate repetition, refine word choices, and ensure a consistent tone and style throughout each article. Verify that the content remains accurate, beginner-friendly, engaging, and well-structured. Produce polished, publication-ready blog articles while preserving all factual information from the original drafts.
    """,

    expected_output= "A polished & improved blog article",

    agent= reviewer_agent

)

# ---------------------------- Crew ----------------------------

crew = Crew(
    
    agents= [researcher_agent, writer_agent, reviewer_agent],

    tasks= [research_task, writing_task, review_task],

    process= Process.sequential,

    verbose= True

)

# ---------------------------- Running The Crew ----------------------------

result = crew.kickoff()

print("Final Output:\n")
print(result)