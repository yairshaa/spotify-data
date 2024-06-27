import json
import pandas as pd


def get_data(songs_dict):
    top_artists_f: dict = {}
    top_songs_f: dict = {}
    song_history_f: dict = {}

    for song in songs_dict:
        date = song["ts"][:10]
        song_name = song["master_metadata_track_name"]
        artist_name = song["master_metadata_album_artist_name"]
        ms_song_played = song["ms_played"]
        # Songs:
        try:
            top_songs_f[song_name][0] += 1
            top_songs_f[song_name][1] += ms_song_played
        except KeyError:
            top_songs_f[song_name] = [1, ms_song_played]
        # Artists:
        try:
            top_artists_f[artist_name] += 1
        except KeyError:
            top_artists_f[artist_name] = 1
        # Song History {Date: Name, Times}:
        try:
            song_history_f[date][song_name] += 1
        except KeyError:
            try:
                song_history_f[date][song_name] = 1
            except KeyError:
                song_history_f[date] = {song_name: 1}


    return top_songs_f, top_artists_f, song_history_f


if __name__ == '__main__':
    with open("endsong_0.json", 'r', encoding='utf-8') as f:
        history = f.read()

    spotify_history = json.loads(history)

    top_songs, top_artists, song_history = get_data(spotify_history)

    top_songs_pd = pd.DataFrame(top_songs)
    top_songs_pd.rename(index={0: 'Times Played', 1: 'Ms Played'}, inplace=True)

    top_artists_pd = pd.Series(top_artists)

    print(song_history)
