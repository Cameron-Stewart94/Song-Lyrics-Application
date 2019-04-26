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
    artist_info = Artist.objects.all()
    song_info = Song.objects.all()
    artist_lst =[]
    song_lst = []
    for i in range(len(artist_info)):
        artist_lst.append(str(artist_info[i].artist).upper())

    for i in range(len(song_info)):
        song_lst.append(str(song_info[i].song).upper())



    return {'artists': artist_lst, 'songs': song_lst}
