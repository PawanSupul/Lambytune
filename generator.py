"""
Song section generator module using LangChain OpenAI.
Generates individual song sections (verses, chorus, bridge, etc.) based on prompts.
"""

from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(temperature=0.85, max_tokens=250)


def generate_section(prompt: str, section: str, rhythm_scheme: str = "AABB", context: str = "") -> str:
    """
    Generate a section of a song based on the provided prompt and section type.
    
    Args:
        prompt (str): The main idea or theme for the song
        section (str): The type of section to generate (e.g., Verse, Chorus, Bridge)
        rhythm_scheme (str): The rhyme pattern to follow (default: "AABB")
        context (str): Additional context from previously generated sections
        
    Returns:
        str: The generated song section lyrics
    """
    section_prompt = f"""
        You are a professional songwriter. Write only the **lyrics** for the section titled **{section}**.
        Do **not** include any section headers (e.g., don't write "Verse 1:" or "Chorus:").
        Just write the body of the lyrics for the section **{section}**.

        Follow this song idea: "{prompt}"

        Write **no more than 2 stanzas** for the section **{section}**.
        Each stanza should follow this rhyme pattern: {rhythm_scheme}. Keep line lengths consistent.
        
        The lyrics should match the style and mood of the song.
        Do **not** include any other section outside of the **{section}**.
        Do **not** repeat the section multiple times.
        Keep it poetic, emotional, and matching the theme while being easy to sing.

        Context (previous lyrics if any):
        "{context}"
        """
    
    response = llm(section_prompt)
    return response