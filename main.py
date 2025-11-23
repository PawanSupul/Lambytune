"""
Lambytune - AI-powered songwriter agent
Main entry point for the application
"""

from agent import generate_song


def main():
    """Main function to run the songwriter agent."""
    print("Welcome to the Songwriter agent!")
    idea = input("Please enter your song idea (e.g., 'a sad ballad about rain'): ")
    
    plan, song = generate_song(idea)
    
    print("\n--- Song Complete! ---")
    print("*" * 64)
    print("===========> Full song lyrics:")
    print(song)


if __name__ == "__main__":
    main()