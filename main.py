from crewai import Crew
from crew_config import creative_director, lyricist, chorus_adjuster, composer, editor
from crew_tasks import define_tasks

def main():
    user_prompt = input("Enter the theme or concept for the song: ")
    agents = {
        "creative_director": creative_director,
        "lyricist": lyricist,
        "chorus_adjuster": chorus_adjuster,
        "composer": composer,
        "editor": editor,
    }

    tasks = define_tasks(agents, user_prompt)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("Final Song Output:\n")
    print(result)


if __name__ == "__main__":
    main()

