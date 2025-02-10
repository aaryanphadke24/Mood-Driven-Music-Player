# main.py
from app.mood_classifier import classify_mood
from app.playlist_generator import generate_playlist

def main():
    print("Welcome to the Mood-Driven Music Playlist Generator!")
    user_input = input("How are you feeling today? Please type a sentence: ")
    
    # Step 1: Classify the mood based on user input
    mood = classify_mood(user_input)
    
    # Step 2: Generate a playlist based on the classified mood
    playlist = generate_playlist(mood)
    
    # Step 3: Display the playlist
    print(f"\nHere is your {mood} playlist:")
    for track in playlist:
        print(f"- {track['name']} by {track['artist']} (Listen: {track['url']})")

if __name__ == "__main__":
    main()
