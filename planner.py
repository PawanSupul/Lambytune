"""
Song planning module using LangChain OpenAI.
Generates structured song plans based on user prompts.
"""

from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

llm = OpenAI(temperature=0.7)


def extract_json_from_response(response: str) -> dict:
    """
    Extract JSON data from LLM response text.
    
    Args:
        response (str): The raw response from the language model
        
    Returns:
        dict: Parsed JSON data
        
    Raises:
        ValueError: If no valid JSON is found or JSON is malformed
    """
    match = re.search(r'\{[\s\S]*\}', response)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in response: {response}\nError: {e}")
    else:
        raise ValueError(f"No valid JSON found in response: {response}")


def plan_song(prompt: str) -> dict:
    """
    Plan a song structure based on the given prompt.
    
    Args:
        prompt (str): The main idea or theme for the song
        
    Returns:
        dict: Song plan containing title, genre, mood, rhythm scheme, and sections
    """
    plan_prompt = f"""
        You are a song planning assistant. Given the idea: "{prompt}", respond in JSON format with the following structure:
        {{
        "title": "...",
        "genre": "...",
        "mood": "...",
        "rhythm_scheme": "AABB",
        "sections": ["Verse 1", "Chorus", "Verse 2", "Chorus", "Bridge", "Chorus"]
        }}
        Do not include anything outside the JSON. Keep it simple and clean.
        The output should be a valid JSON object with the song plan.
        """
    
    response = llm(plan_prompt)
    plan_data = extract_json_from_response(response)
    return plan_data


# Common song structures for reference:
#
# 1. Verse-Chorus-Verse-Chorus (VCVC)
#    Simple, catchy structure used in pop music
#    Example: "Back to Black" by Amy Winehouse
#
# 2. Verse-Chorus-Verse-Chorus-Bridge-Chorus (VCVCBC)
#    Most common structure in contemporary music
#    Examples: "Back for Good" by Take That, "Someone Like You" by Adele
#
# 3. Verse-Verse-Bridge-Verse (AABA)
#    Classic structure from early 20th-century American pop
#    Examples: "We Can Work It Out" by The Beatles, "Still Rock and Roll to Me" by Billy Joel