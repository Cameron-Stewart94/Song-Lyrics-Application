from django.db import models

# Create your models here.
class Artist(models.Model):
    artist = models.CharField(max_length=264, null=True)


    def __str__(self):
        return self.artist


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.CharField(max_length=264)
    lyrics = models.TextField(null=True, blank=True)
    searches = models.IntegerField(default=1)

    class Meta:
        unique_together = ['artist', 'song']

    def __str__(self):
        return self.song
