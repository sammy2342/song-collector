from audioop import reverse
from django.db import models

from django.urls import reverse
# Create your models here.
class Song(models.Model): 
    song = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    released = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self): 
        return self.song

    def get_absolute_url(self): 
        return reverse('detail', kwargs={'song_id': self.id})