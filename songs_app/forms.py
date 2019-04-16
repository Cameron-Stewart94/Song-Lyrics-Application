from django import forms
from songs_app.models import Artist, Song

class ArtistChoice(forms.ModelForm):

    class Meta():
        model = Artist
        fields = '__all__'

class SongChoice(forms.ModelForm):
    class Meta():
        model = Song
        fields = ('song',)
