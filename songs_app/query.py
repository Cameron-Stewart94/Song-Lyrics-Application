from songs_app.models import Artist, Song
from random import randint
from collections import defaultdict

def random_song_generator():
    # Function generates a random song from database
    song_query = Song.objects.all()
    number_of_songs = len(song_query)
    random_number = randint(0, number_of_songs - 1)
    artist = song_query[random_number].artist
    song = song_query[random_number].song
    lyrics = song_query[random_number].lyrics
    return {'artist': artist, 'song': song, 'lyrics': lyrics}

def database_check():
    # Function queries database and lists all artists and songs in the database
    artist_information = Artist.objects.all()
    top_song_information = Song.objects.all()
    artist_lst =[str(artist_information[i].artist).upper() for i in range(len(artist_information))]
    song_lst = [str(top_song_information[i].artist).upper() for i in range(len(top_song_information))]




    return {'artists': artist_lst, 'songs': song_lst}
