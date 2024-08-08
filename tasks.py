from crewai import Task
from tools import tool
from agents import news_researcher, news_writer  # Corrected variable name

# Researcher task
research_task = Task(
    description="Find the latest news",
    expected_output="A comprehensive three-paragraph-long report on the latest news",
    tools=[tool],
    agent=news_researcher  # Corrected variable name
)

# Writing task with language model configuration
write_task = Task(
    description="Write news",
    expected_output="A comprehensive three-paragraph-long report on the latest news",
    tools=[tool],
    agent=news_writer,
    output_file='new-blog-post.md'
)
