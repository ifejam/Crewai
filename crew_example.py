import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

# Defining my agents and roles.
researcher = Agent(
    role="Senior AI Tutor",
    goal="Develop ideas for teaching someone new to the subject",
    backstory="""you are a Senior A
    i tutor.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
)
writer = Agent(
    role="writer",
    goal="Use the Researchers ideas to write a piece of text to explain the topic",
    backstory="""You are a renowned Content Writter, known for
    your insightful and engaging articles""",
    verbose=True,
    allow_delegation=False,
)
Examiner = Agent(
    role="examiner",
    goal="""Create 2-3 test questions based on the written text and provide correct answers.
    Essentially, test if a student understands the text""",
    backstory="""You are an examiner who sets test questions for students""",
    verbose=True,
    allow_delegation=False,
)

# assign a task to each agent.

task1 = Task(
    description="""Explain the primary objective of Artificial Intelligence (AI) and how it differs from traditional computer programs.
    Provide examples to illustrate the types of tasks that AI is designed to perform.""",
    agent=researcher,
)
task2 = Task(
    description="""Compare and contrast Narrow AI (Weak AI) and General AI (Strong AI). 
    Elaborate on their respective capabilities, and give real-world examples to illustrate their applications in different domains.""",
    agent=writer,
)
task3 = Task(
    description="""Create 2-3 test questions based on the written text and provide correct answers. 
    Essentially, test if a student understands the text.""",
    agent=Examiner,
)
crew = Crew(
    agents=[researcher, writer, Examiner],
    tasks=[task1, task2, task3],
    verbose=2,
)
# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
