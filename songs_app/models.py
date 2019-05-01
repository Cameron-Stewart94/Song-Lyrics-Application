from django.db import models

class Artist(models.Model):
    # Class creates Artist model in the database
    artist = models.CharField(max_length=264, null=True)

    def __str__(self):
        return self.artist


class Song(models.Model):
    # Class creates Song model in database and is linked to Artist model
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # artist is linked to Artist model, through a ForeignKey (One to many field)
    song = models.CharField(max_length=264)
    lyrics = models.TextField(null=True, blank=True)
    searches = models.IntegerField(default=1)

    class Meta:
        # Meta class ensures repeat entries are not stored in database
        unique_together = ['artist', 'song']
        # Unique together ensures that either artist or song must be unique to save to database

    def __str__(self):
        return self.song
