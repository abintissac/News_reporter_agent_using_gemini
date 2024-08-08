from crewai import Agent
from tools import tool

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the genAI models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Create a senior research agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Find the latest news",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

# Create a writer agent with custom tools responsible for writing news
news_writer = Agent(
    role="Writer",
    goal="Write news",
    verbose=True,
    memory=True,
    backstory=("With a flair for simplifying complex topics, you craft"),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
