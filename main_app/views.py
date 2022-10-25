from urllib import request
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Song



def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

class SongIndex(ListView): 
    model = Song
    template_name = 'songs/index.html'

def songs_detail(request, song_id): 
    song = Song.objects.get(id=song_id)
    return render(request, 'songs/detail.html', { 'song': song })

class SongCreate(CreateView): 
    model = Song 
    fields = '__all__'
    success_url = '/songs/'

class SongUpdate(UpdateView): 
    model = Song 
    fields = ['song', 'name', 'description', 'released']

class SongDelete(DeleteView): 
    model = Song 
    success_url = '/songs/'

# Create your views here.
