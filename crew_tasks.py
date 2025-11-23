from crewai import Task

def define_tasks(agents, prompt):
    task_list = [
        Task(
            description=f"Plan a structured song outline (title, mood, genre, sections) for: {prompt}. Respond in JSON format.",
            agent=agents["creative_director"],
            expected_output="A JSON object with title, genre, mood, rhyme scheme, and sections."
        ),
        Task(
            description="Write each section of the song based on the structure provided.",
            agent=agents["lyricist"],
            expected_output="Full lyrics for each section, no chords yet."
        ),
        Task(
            description="Ensure the chorus sections are identical as much as possible across the song.",
            agent=agents["chorus_adjuster"],
            expected_output="Lyrics with consistent chorus sections."
        ),
        Task(
            description="Add chords (in C major) above each lyric line of the adjusted lyrics with identical choruses.",
            agent=agents["composer"],
            expected_output="Lyrics with chords aligned to each line."
        ),
        Task(
            description="Polish the final output, ensure consistent formatting and rhyme, and eliminate duplicates.",
            agent=agents["editor"],
            expected_output="Final song ready for display or export."
        ),
    ]
    return task_list