from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Artist

from django.http import HttpResponse
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

    # def get(self,request):
    #     return HttpResponse('Spotify Home')
    #     #what is returned here is the returned object


class About(TemplateView):
    template_name = 'about.html'
    # def get(self,request):
    #     return HttpResponse('spotify about')


class Base(TemplateView):
    template_name = 'base.html'


class ArtistList(TemplateView):
    template_name = 'artist_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # SELECT * FROM main_app_artist
        context['artists'] = Artist.objects.all()

        return context
# unlimited arguements in **kwargs, like spread operator


class Song:
    def __init__(self, name, artist):
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
