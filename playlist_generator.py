# app/playlist_generator.py
from app.music_api import fetch_music_by_mood

def generate_playlist(mood):
    """
    Given a mood, generate a playlist from Spotify based on that mood.
    """
    print(f"Generating playlist for mood: {mood}")
    
    # Determine the genre based on the mood
    if mood == "happy":
        genre = "pop"
    elif mood == "sad":
        genre = "indie"
    elif mood == "energetic":
        genre = "rock"
    else:
        genre = "chill"
    
    # Fetch playlist from Spotify based on the mood
    playlist = fetch_music_by_mood(genre)
    
    return playlist
