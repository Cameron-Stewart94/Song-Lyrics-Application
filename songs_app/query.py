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
    # Function queries database and lists all artists and songs stored in the database
    artist_info = Artist.objects.all()
    song_info = Song.objects.all()
    artist_lst =[]
    song_lst = []
    for i in range(len(artist_info)):
        artist_lst.append(str(artist_info[i].artist).upper())

    for i in range(len(song_info)):
        song_lst.append(str(song_info[i].song).upper())

    return {'artists': artist_lst, 'songs': song_lst}


def top_songs_generator():
    count_query = Song.objects.order_by('-searches')
    # Querys songs and orders them by number of searches in reverse order
    artist_lst = []
    song_lst = []
    searches_lst = []
    for i in range(len(count_query)):
        artist_lst.append(count_query[i].artist)
        song_lst.append(count_query[i].song)
        searches_lst.append(count_query[i].searches)
    # Appends song information to corresponding list from most searched song to least searhced song
    return {'artist_lst': artist_lst, 'song_lst': song_lst, 'searches_lst': searches_lst}
