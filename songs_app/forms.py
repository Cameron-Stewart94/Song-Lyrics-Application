from django import forms
from songs_app.models import Artist, Song

class ArtistChoice(forms.ModelForm):
# Class creates form for artist choice and links to Artist model

    class Meta():
        model = Artist
        fields = '__all__'
        # Links to all Artist fields (Only one in this case)

        labels = {'artist': ''}
        widgets = {
        'artist': forms.TextInput(attrs={'placeholder': 'Enter artist here'}),
    }
        # Removes label and adds placeholder to form


class SongChoice(forms.ModelForm):
    # Class creates form for song choice and links to Song model

    class Meta():
        model = Song
        fields = ('song',)
        # Links only to song field in Song model as artist fiels is linked to Artist model through a foreign key
        labels = {'song': ''}
        widgets = {
        'song': forms.TextInput(attrs={'placeholder': 'Enter song here'}),
    }
        # Removes label and adds placeholder to form
