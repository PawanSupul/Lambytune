"""
Task Definition Module for LambyTune Song Creation Workflow

This module defines the sequential tasks that AI agents execute to create a complete song,
from initial structure planning to final polishing.
"""

from typing import Dict, List
from crewai import Task, Agent


def define_tasks(agents: Dict[str, Agent], prompt: str) -> List[Task]:
    """
    Create a list of tasks for the song creation workflow.
    
    Args:
        agents: Dictionary mapping agent names to Agent instances
        prompt: User's theme or concept for the song
        
    Returns:
        List of Task objects defining the song creation pipeline
    """
    task_list = [
        # Task 1: Creative Direction - Define song structure and mood
        Task(
            description=f"Plan a structured song outline (title, mood, genre, sections) for: {prompt}. Respond in JSON format.",
            agent=agents["creative_director"],
            expected_output="A JSON object with title, genre, mood, rhyme scheme, and sections."
        ),
        
        # Task 2: Lyric Writing - Create verses and choruses based on structure
        Task(
            description="Write each section of the song based on the structure provided.",
            agent=agents["lyricist"],
            expected_output="Full lyrics for each section, no chords yet."
        ),
        
        # Task 3: Chorus Standardization - Ensure chorus consistency
        Task(
            description="Ensure the chorus sections are identical as much as possible across the song.",
            agent=agents["chorus_adjuster"],
            expected_output="Lyrics with consistent chorus sections."
        ),
        
        # Task 4: Musical Composition - Add chord progressions
        Task(
            description="Add chords (in C major) above each lyric line of the adjusted lyrics with identical choruses.",
            agent=agents["composer"],
            expected_output="Lyrics with chords aligned to each line."
        ),
        
        # Task 5: Final Editing - Polish and format the complete song
        Task(
            description="Polish the final output, ensure consistent formatting and rhyme, and eliminate duplicates.",
            agent=agents["editor"],
            expected_output="Final song ready for display or export."
        ),
    ]
    return task_list