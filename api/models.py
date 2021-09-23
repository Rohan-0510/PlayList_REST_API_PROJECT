from django.db import models

class Playlist(models.Model):
    index = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    title=models.CharField(max_length=50)
    danceability=models.FloatField(null=True)
    energy=models.FloatField(null=True)
    key=models.IntegerField(null=True)
    loudness=models.FloatField(null=True)
    mode=models.IntegerField(null=True)
    acousticness=models.FloatField(null=True)
    instrumentalness=models.FloatField(null=True)
    liveness=models.FloatField(null=True)
    valence=models.FloatField(null=True)
    tempo=models.FloatField(null=True)
    duration_ms=models.BigIntegerField(null=True)
    time_signture=models.IntegerField(null=True)
    num_bars=models.IntegerField(null=True)
    num_sections=models.IntegerField(null=True)
    num_segments=models.IntegerField(null=True)
    classes=models.IntegerField(null=True)
    star_rating=models.IntegerField(null=True)

    def __str__(self):
        return self.title

