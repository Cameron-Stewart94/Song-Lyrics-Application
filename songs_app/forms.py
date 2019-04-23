from django import forms
from songs_app.models import Artist, Song

class ArtistChoice(forms.ModelForm):

    class Meta():
        model = Artist
        fields = '__all__'

        labels = {'artist': ''}
        widgets = {
        'artist': forms.TextInput(attrs={'placeholder': 'Enter artist here'}),
    }



class SongChoice(forms.ModelForm):
    class Meta():
        model = Song
        fields = ('song',)
        labels = {'song': ''}
        widgets = {
        'song': forms.TextInput(attrs={'placeholder': 'Enter song here'}),
    }
