"""
LambyTune - AI-Powered Song Creation Tool

This module serves as the main entry point for the LambyTune application,
which uses CrewAI to orchestrate multiple AI agents for collaborative song creation.
"""

from crewai import Crew
from crew_config import creative_director, lyricist, chorus_adjuster, composer, editor
from crew_tasks import define_tasks


def main() -> None:
    """
    Main function that orchestrates the song creation process.
    
    Prompts user for input and coordinates AI agents to create a complete song
    with lyrics, structure, and chord progressions.
    """
    # Get user input for song theme/concept
    user_prompt = input("Enter the theme or concept for the song: ")
    
    # Define agent roles for the song creation workflow
    agents = {
        "creative_director": creative_director,
        "lyricist": lyricist,
        "chorus_adjuster": chorus_adjuster,
        "composer": composer,
        "editor": editor,
    }

    # Create tasks based on agents and user prompt
    tasks = define_tasks(agents, user_prompt)

    # Initialize crew with agents and tasks
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    # Execute the song creation workflow
    result = crew.kickoff()
    
    # Display final output
    print("Final Song Output:\n")
    print(result)


if __name__ == "__main__":
    main()

