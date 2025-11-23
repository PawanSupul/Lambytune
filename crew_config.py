"""
AI Agent Configuration for LambyTune Song Creation

This module defines the AI agents responsible for different aspects of song creation,
including creative direction, lyric writing, composition, and editing.
"""

from typing import Optional
from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables (API keys, etc.)
load_dotenv()

# Initialize language model with creative temperature setting
llm = ChatOpenAI(model="gpt-4", temperature=0.8)

# Creative Director Agent - Plans song structure and emotional flow
creative_director = Agent(
    role="Creative Director",
    goal="Define a compelling structure for the song",
    backstory="You are responsible for planning the flow and emotional arc of the song.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
)

# Lyricist Agent - Creates poetic and engaging lyrics
lyricist = Agent(
    role="Lyricist",
    goal="Write poetic and emotionally powerful lyrics",
    backstory="You turn structure and prompts into flowing, rhymed verses and choruses.",
    verbose=True,
    llm=llm,
)

# Composer Agent - Adds musical harmony and chord progressions
composer = Agent(
    role="Composer",
    goal="Add chords above each line based on the song's mood and rhyme",
    backstory="You are a musical genius who matches harmonies with words.",
    verbose=True,
    llm=llm,
)

# Editor Agent - Polishes and refines the final output
editor = Agent(
    role="Editor",
    goal="Polish lyrics for flow, remove repetitions, and ensure structure integrity",
    backstory="You review and refine the lyrics to make them stage-ready.",
    verbose=True,
    llm=llm,
)

# Chorus Adjuster Agent - Ensures chorus consistency throughout the song
chorus_adjuster = Agent(
    role="Chorus Adjuster",
    goal="Ensure the chorus sections in the song are identical as much as possible",
    backstory="You focus on standardizing chorus sections to maintain consistency in the song's structure.",
    verbose=True,
    llm=llm,
)


