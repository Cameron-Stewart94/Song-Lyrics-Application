from songs_app.models import Artist, Song
from random import randint

def a():

    b = Song.objects.all()
    no_of_songs = len(b)
    random_number = randint(0, no_of_songs - 1)
    lyrics = b[random_number].lyrics
    artist = b[random_number].artist
    song = b[random_number].song
    return {'artist': artist, 'song': song, 'lyrics': lyrics}
