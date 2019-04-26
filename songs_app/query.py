from songs_app.models import Artist, Song
from random import randint
from collections import defaultdict

def a():

    b = Song.objects.all()
    no_of_songs = len(b)
    random_number = randint(0, no_of_songs - 1)
    lyrics = b[random_number].lyrics
    artist = b[random_number].artist
    song = b[random_number].song
    return {'artist': artist, 'song': song, 'lyrics': lyrics}

def top_song():
    art = Song.objects.all()
    artists_and_songs = defaultdict(list)
    for artist in art:
        artists_and_songs[artist.artist].append(artist.song)

    return artists_and_songs
