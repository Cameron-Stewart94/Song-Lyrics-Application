from django.shortcuts import render
from django.views.generic import View, TemplateView
from songs_app.forms import SongChoice, ArtistChoice
from django.http import HttpResponseRedirect, HttpResponse
from songs_app.lyrics_generator import Lyrics
from songs_app.models import Artist, Song
from songs_app.query import a, top_song

# Create your views here.
def index(request):
    artist_form = ArtistChoice()
    song_form = SongChoice()


    if request.method == 'POST':
        artist_form = ArtistChoice(data=request.POST)
        song_form = SongChoice(data=request.POST)

        if artist_form.is_valid() and song_form.is_valid():
            artist_value = artist_form.cleaned_data['artist']
            song_value = song_form.cleaned_data['song']

            info_dic = top_song()

            if artist_value.upper() in info_dic.keys() and song_value.upper() in info_dic[artist_value]:
                info = Song.objects.all()
                artist = info.artist
                song = info.song
                lyrics = info.lyrics

                return render(request, 'songs_app/lyrics.html', {'lyrics': lyrics, 'artist': artist, 'song': song})

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
    return render(request, 'songs_app/lyrics.html')




def random_song(request):
    msg = a()
    return render(request, 'songs_app/random_song.html', {'artist': msg['artist'], 'song': msg['song'], 'lyrics': msg['lyrics']} )


def top_songs(request):
    test = top_song()
    return render(request, 'songs_app/top_songs.html', {'test': test})
