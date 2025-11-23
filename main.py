from agent import generate_song

def main():
    print("Welcome to the Songwriter agent!")
    idea = input("Please enter your song idea (e.g., 'a sad balladd about rain'): ")
    plan, song = generate_song(idea)
    print("\n--- Song Complete! ---")
    # print(plan)
    print("****************************************************************")
    print("===========> Full song lyrics:")
    print(song)

if __name__ == "__main__":
    main()