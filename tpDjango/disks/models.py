from django.db import models


# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100, null=True)
    milliseconds = models.IntegerField(null=True)
    bytes = models.IntegerField(null=True)
    unitPrice = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "track"
        ordering = ['name', 'composer']

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album"
        ordering = ['title', 'artist']

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "artist"
        ordering = ['name']

    def __str__(self):
        return self.name
