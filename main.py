import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = "http://localhost:3000"

scope = "user-read-recently-played"

# Authenticate using SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))


def get_user_top_artists(time_range):  # time range - short_term (4 weeks), medium_term (6 months), long_term (All Time)
    results = sp.current_user_top_artists(limit=10, time_range=time_range)
    for idx, artist in enumerate(results['items']):
        return f"{idx + 1}. {artist['name']}"


def get_user_top_tracks(time_range):  # time range - short_term (4 weeks), medium_term (6 months), long_term (All Time)
    results = sp.current_user_top_tracks(limit=10, time_range=time_range)
    for idx, artist in enumerate(results['items']):
        return f"{idx + 1}. {artist['name']}"


def get_recently_played_tracks():
    results = sp.current_user_recently_played(limit=50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        played_at = item['played_at']
        print(
            f"{idx + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])} at {played_at}")


def get_track_data(song_name) -> list:
    track_results = sp.search(q=song_name, type='track', limit=1)['tracks']['items'][0]
    length_s = track_results["duration_ms"] // 1000
    length: str = f"{length_s // 60}:{length_s % 60}"
    artist: str = track_results["album"]["artists"][0]["name"]

    return [length, artist]


track_data = get_track_data("HIGHEST IN THE ROOM")
