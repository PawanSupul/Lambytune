from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

llm = OpenAI(temperature=0.7)


def extract_json_from_response(response: str) -> dict:
    match = re.search(r'\{[\s\S]*\}', response)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in response: {response}\nError: {e}")
    else:
        raise ValueError(f"No valid JSON found in response: {response}")


def plan_song(prompt: str) -> dict:
    plan_prompt = f"""
        Your are a song planning assistant. Given the idea: "{prompt}", respond in JSON format with the following structure:
        {{
        "title": "...",
        "genre": "...",
        "mood": "...",
        "rhythm_scheme": "AABB",
        "sections": ["Verse 1", "Chorus", "Verse 2", "Chorus", "Bridge", "Chorus"],
        }}
        Do not include anything outside the JSON. Keep it simple and clean.
        The output should be a valid JSON object with the song plan."""
    
    response = llm(plan_prompt)
    plan_data = extract_json_from_response(response)
    return plan_data



""" Song Structures:
1. Verse-Chorus-Verse-Chorus (ACAC)
this structure is not only catchy and accessible but also radio-friendly:
Back to Black by Amy Winehouse

2. Verse-Chorus-Verse-Chorus-Bridge-Chorus (ACACBC)
inclusion of a bridge amplifies the emotional impact of the song, making it a preferred choice among contemporary songwriters:
Back for Good by Take That and Someone Like You by Adele. 

3. Verse-Verse-Bridge-Verse (AABA)
held prominence in early 20th-century American pop music: 
We Can Work It Out by The Beatles and Still Rock and Roll to Me by Billy Joel.

"""