from crewai import Crew, Process
from tasks import research_task, write_task  # Updated import after renaming
from agents import news_researcher, news_writer  # Corrected variable name

# Forming tech-focused crew with some enhanced configuration
crew = Crew(
    agents=[news_researcher, news_writer],  # Corrected variable name
    tasks=[research_task, write_task],
    process=Process.sequential,
)

result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
