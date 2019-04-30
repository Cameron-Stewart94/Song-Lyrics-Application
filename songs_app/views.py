from django.shortcuts import render
from django.views.generic import View, TemplateView
from songs_app.forms import SongChoice, ArtistChoice
from django.http import HttpResponseRedirect, HttpResponse
from songs_app.lyrics_generator import Lyrics
from songs_app.models import Artist, Song
from songs_app.query import a, top_song
from django.db.models import F

def index(request):
    artist_form = ArtistChoice()
    song_form = SongChoice()


    if request.method == 'POST':
        artist_form = ArtistChoice(data=request.POST)
        song_form = SongChoice(data=request.POST)

        if artist_form.is_valid() and song_form.is_valid():
            artist_value = artist_form.cleaned_data['artist']
            song_value = song_form.cleaned_data['song']

            top_song_info = top_song()

            if artist_value.upper() in top_song_info['artists'] and song_value.upper() in top_song_info['songs']:
                em = Song.objects.filter(artist__artist__iexact=artist_value).filter(song__iexact=song_value)
                Song.objects.filter(artist__artist__iexact=artist_value).filter(song__iexact=song_value).update(searches=F('searches')+1)

                return render(request, 'songs_app/lyrics.html', {'artist': em[0].artist, 'song': em[0].song, 'lyrics': em[0].lyrics})

            else:
                web_lyrics = Lyrics(artist_value, song_value)
                try:
                    web_lyrics.fetch_data()
                except:
                    return render(request, 'songs_app/invalid_choice.html')
                else:
                    song = song_form.save(commit=False)
                    artist, created = Artist.objects.get_or_create(artist = web_lyrics.artist_name)
                    song.lyrics = web_lyrics.song_lyrics
                    song.artist = artist
                    song.song = web_lyrics.song_name
                    case_artist = web_lyrics.artist_name

                    try:
                        song.save()
                    except:
                        return render(request, 'songs_app/lyrics.html', {'lyrics': song.lyrics, 'artist': case_artist, 'song': song.song})

        return render(request, 'songs_app/lyrics.html', {'lyrics': song.lyrics, 'artist': case_artist, 'song': song.song})


    else:
        print('Invalid Information Provided')
    return render(request, 'songs_app/index.html', {'artist_form': artist_form, 'song_form': song_form})

def lyrics(request):
    pass




def random_song(request):
    msg = a()
    return render(request, 'songs_app/random_song.html', {'artist': msg['artist'], 'song': msg['song'], 'lyrics': msg['lyrics']} )


def top_songs(request):
    count_query = Song.objects.order_by('-searches')
    artist_lst = []
    song_lst = []
    searches_lst = []
    for i in range(len(count_query)):
        artist_lst.append(count_query[i].artist)
        song_lst.append(count_query[i].song)
        searches_lst.append(count_query[i].searches)
    return render(request, 'songs_app/top_songs.html', {'artist_lst': artist_lst, 'song_lst' : song_lst, 'searches_lst': searches_lst, 'range' : range(10)})


def test(request):
    a = 'eminem'
    b = 'stan'
    c = top_song()

    if a.upper() in c['artists'] and b.upper() in c['songs']:
        em = Song.objects.filter(artist__artist__iexact=a).filter(song__iexact=b)
    return render(request, 'songs_app/test.html', {'here': em[0].lyrics})

def top_lyrics(request):
    return render(request, 'songs_app/top_lyrics.html', {'artist': 'a', 'song': 'b', 'lyrics': 'c'})
