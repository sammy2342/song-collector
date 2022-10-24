from django.shortcuts import render
from django.http import HttpResponse

class Song: 
    def __init__(self, song, name, released, description):
        self.song = song
        self.name = name 
        self.year = released
        self.description = description

songs = [ 
    Song('My Way', 'Frank Sinatra', 1978, 'represents the quintessentially American outlook that nothing in life matters more than living on your own terms.'),
    Song('Cant Help Flling in Love', 'Elis Presley', 1961, "The song speaks about the singer's feeling towards a girl for whom he is falling in love uncontrollably."),
]

def home(request): 
    return HttpResponse('<h1>Hello Welcome</h1>')

def about(request): 
    return render(request, 'about.html')

def songs_index(request): 
    return render(request, 'songs/index.html', { 'songs': songs })

# Create your views here.
