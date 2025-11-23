"""
Agent module for generating complete songs using a planner and generator.
Handles the main orchestration of the song creation process.
"""

from planner import plan_song
from generator import generate_section
import re


def generate_song(prompt: str) -> tuple[dict, str]:
    """
    Generate a complete song based on the provided prompt.
    
    Args:
        prompt (str): The main idea or theme for the song
        
    Returns:
        tuple[dict, str]: A tuple containing the song plan and generated lyrics
    """
    # Step 1: Plan the song structure
    plan = plan_song(prompt)

    title = plan.get("title", "Untitled Song")
    genre = plan.get("genre", "Unknown Genre")
    mood = plan.get("mood", "Neutral Mood")
    rhythm_scheme = plan.get("rhythm_scheme", "AABB")
    sections = plan.get("sections", [])

    print("\nSONG PLAN:")
    print(f"Title: {title}")
    print(f"Genre: {genre}")
    print(f"Mood: {mood}")
    print(f"Sections: {sections}")

    lyrics = f'\n\n# {title}\n\n'
    full_text_so_far = ""
    chorus = ""

    for section in sections:
        print(f"\nGenerating section: {section}...")
        
        if section.lower() == "chorus":
            # Reuse existing chorus or generate a new one
            if chorus:
                part = chorus
            else:
                chorus_generated = generate_section(prompt, section, rhythm_scheme, full_text_so_far)
                chorus = chorus_generated.strip()
                part = chorus
        else:
            # Generate other sections normally
            part = generate_section(prompt, section, rhythm_scheme, full_text_so_far)
        
        print(part)

        # Clean section headers from the generated content
        pattern = rf"^\s*{re.escape(section)}\s*[:\-]*\s*"
        cleaned_part = re.sub(pattern, '', part.strip(), flags=re.IGNORECASE | re.MULTILINE).strip()

        lyrics += f"\n\n## {section}:\n{cleaned_part}\n"
        full_text_so_far += f"\n\n{cleaned_part}\n"
        
    return plan, lyrics
