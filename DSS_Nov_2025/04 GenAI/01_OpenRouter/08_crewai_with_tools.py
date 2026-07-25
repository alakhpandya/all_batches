from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os

from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

# ----------------------- LLM -----------------------
deepseek_llm = LLM(

    model = "openrouter/deepseek/deepseek-chat",

    api_key = os.getenv("OPENROUTER_API_KEY"),

    base_url = "https://openrouter.ai/api/v1",

    # max_tokens= 200

    temperature= 0.7
)

nemotron_llm = LLM(

    model= "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",

    api_key = os.getenv("OPENROUTER_API_KEY"),

    base_url = "https://openrouter.ai/api/v1",

    # max_tokens= 200

    temperature= 0.5
)

# ----------------------- Tools -----------------------

goolge_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()


# ----------------------- Agents -----------------------

researcher = Agent(

    role = "AI researcher",

    goal = "Find out the trending AI topics related to AI that can go viral",

    backstory = """
    You are an expert research who is working with a highly popular blogger who has more than 1 million followers since last 5 years.
    
    You search & find out hot topics around artificial intelligence, machine learning, robotics, generative AI etc. which are currently getting viral on social media platforms and return a detailed research report of top-3 topics in the descending order of the probability of their going viral.
    """,

    verbose = True,

    llm = nemotron_llm,

    tools = [goolge_search_tool, web_scraping_tool]
)


writer = Agent(

    role = "AI blog writer",

    goal = "Write simple & engaging blog articles on the topics provided with their research summary",

    backstory = """
    You are a senior blog writer in team of a highly popular blogger.

    You write beginner-friendly and engaging content that has very high probability to go viral on different social media platforms.
    """,

    verbose = True,

    llm = deepseek_llm
)

reviewer = Agent(

    role = "Content reviewer",

    goal = "Improve the quality and readability of the given blog article",

    backstory = """
    You are a senior content reviewer at a leading blogging company who has expertise in reviewing, improving and editing blog articles provided.

    You improve grammar, structure, readiblity & quality of the article so to improve their probability of getting viral.
    """,

    verbose = True,

    llm = nemotron_llm
)

# ----------------------- Tasks -----------------------

research_task = Task(

    description= """
    Research the latest trends in Artificial Intelligence and identify the top 3 most relevant and widely discussed topics based on recent developments, industry adoption, research publications, and community interest. For each topic, prepare a comprehensive research summary that includes an overview, why the topic is currently trending, key concepts, important technologies or tools involved, real-world applications, recent advancements, benefits, challenges, and future outlook. Ensure that the information is accurate, well-structured, objective, and easy to understand. The research summary should provide sufficient depth for another agent to create a high-quality blog article without requiring any additional research.
    """,

    expected_output= "A clear and detailed research summary report of top-3 topics",

    agent= researcher

)

writing_task = Task(

    description= """
    Using the research summary provided by the previous task, write a separate blog article for each of the identified AI topics. Each article should be beginner-friendly, engaging, informative, and concise while maintaining technical accuracy. Use simple language, an attention-grabbing introduction, clear headings and subheadings, short paragraphs, practical examples or analogies where appropriate, and a motivating conclusion. Do not introduce information that is not supported by the provided research summary. The articles should be original, easy to read, and optimized for audience engagement.
    """,

    expected_output= "A complete blog article",

    agent= writer

)

review_task = Task(

    description= """
    Review the blog articles produced by the writing task and improve their overall quality without changing their intended meaning. Correct grammatical, spelling, punctuation, and formatting errors. Enhance sentence clarity, readability, coherence, and logical flow. Improve transitions between sections, eliminate repetition, refine word choices, and ensure a consistent tone and style throughout each article. Verify that the content remains accurate, beginner-friendly, engaging, and well-structured. Produce polished, publication-ready blog articles while preserving all factual information from the original drafts.
    """,

    expected_output= "A polished & improved blog article",

    agent= reviewer

)

# ----------------------- Crew -----------------------

crew = Crew(

    agents= [researcher, writer, reviewer],

    tasks= [research_task, writing_task, review_task],

    process= Process.sequential,

    verbose= True
)

# ----------------------- Running the Crew -----------------------

result = crew.kickoff()

print("::Final Output::")
print(result)