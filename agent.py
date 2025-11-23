from planner import plan_song
from generator import generate_section
import re

def generate_song(prompt: str) -> str:
    # Step 1: Plan the song
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
            # If the section is a chorus, we will generate it separately
            if chorus:
                # If we already have a chorus, we will use it
                part = chorus
            else:
                chorus_generated = generate_section(prompt, section, rhythm_scheme, full_text_so_far)
                chorus = chorus_generated.strip()
                part = chorus
        else:
        # For other sections, we generate them normally
            part = generate_section(prompt, section, rhythm_scheme, full_text_so_far)
        print(part)

        pattern = rf"^\s*{re.escape(section)}\s*[:\-]*\s*"
        cleaned_part = re.sub(pattern, '', part.strip(), flags=re.IGNORECASE | re.MULTILINE).strip()

        lyrics += f"\n\n## {section}:\n{cleaned_part}\n"
        full_text_so_far += f"\n\n{cleaned_part}\n"
        
    return plan, lyrics
