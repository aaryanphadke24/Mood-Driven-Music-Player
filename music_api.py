# app/music_api.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# Setup Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

def fetch_music_by_mood(genre):
    """
    Fetch music from Spotify based on the genre (mood).
    """
    print(f"Fetching {genre} music from Spotify...")
    
    # Search for tracks by genre
    results = sp.search(q=f'genre:{genre}', type='track', limit=10)
    
    # Extract relevant track info
    tracks = results['tracks']['items']
    playlist = [
        {"name": track['name'], "artist": track['artists'][0]['name'], "url": track['external_urls']['spotify']}
        for track in tracks
    ]
    
    return playlist
