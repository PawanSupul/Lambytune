from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0.8)

creative_director = Agent(
    role="Creative Director",
    goal="Define a compelling structure for the song",
    backstory="You are responsible for planning the flow and emotional arc of the song.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
)

lyricist = Agent(
    role="Lyricist",
    goal="Write poetic and emotionally powerful lyrics",
    backstory="You turn structure and prompts into flowing, rhymed verses and choruses.",
    verbose=True,
    llm=llm,
)

composer = Agent(
    role="Composer",
    goal="Add chords above each line based on the song's mood and rhyme",
    backstory="You are a musical genius who matches harmonies with words.",
    verbose=True,
    llm=llm,
)

editor = Agent(
    role="Editor",
    goal="Polish lyrics for flow, remove repetitions, and ensure structure integrity",
    backstory="You review and refine the lyrics to make them stage-ready.",
    verbose=True,
    llm=llm,
)

chorus_adjuster = Agent(
    role="Chorus Adjuster",
    goal="Ensure the chorus sections in the song are identical as much as possible.",
    backstory="You focus on changing the chorus sections to make them identical, ensuring consistency in the song's structure.",
    verbose=True,
    llm=llm,
)


