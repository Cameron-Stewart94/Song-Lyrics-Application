from django.shortcuts import render
from django.views.generic import View, TemplateView
from songs_app.forms import SongChoice, ArtistChoice
from django.http import HttpResponseRedirect, HttpResponse
from songs_app.lyrics_generator import Lyrics
from songs_app.models import Artist, Song

# Create your views here.
def index(request):
    artist_form = ArtistChoice()
    song_form = SongChoice()


    if request.method == 'POST':
        artist_form = ArtistChoice(data=request.POST)
        song_form = SongChoice(data=request.POST)

        if artist_form.is_valid() and song_form.is_valid():
            artist, created = Artist.objects.get_or_create(**artist_form.cleaned_data)
            song = song_form.save(commit=False)
            web_lyrics = Lyrics(str(artist.artist), str(song.song))
            web_lyrics.fetch_data()
            song.lyrics = web_lyrics.song_lyrics

            song.song = web_lyrics.song_name
            case_artist = web_lyrics.artist_name

            song.save()





            return render(request, 'songs_app/lyrics.html', {'lyrics': song.lyrics, 'artist': case_artist, 'song': song.song})





    else:
        print('Invalid Information Provided')
    return render(request, 'songs_app/index.html', {'artist_form': artist_form, 'song_form': song_form})

def lyrics(request):
    return render(request, 'songs_app/lyrics.html')
