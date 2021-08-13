from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from django.http import HttpResponse
# Create your views here.

class Song:
    def __init__(self,name,artist):
        self.name = name
        self.artist = artist

songs = [
  Song("Happy Inc", "Gorillaz"),
  Song("That one fallout boy song", "Panic! At The Disco"),
  Song("The Joji Song", "Joji"),
]

class SongList(TemplateView):
    template_name = 'song_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = songs

        return context
