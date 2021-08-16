from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
# if has a form the view will go on .edit, all others .base except DetailView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, Song
from django.urls import reverse

from django.http import HttpResponse
# Create your views here.


class HomePage(TemplateView):
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
        # to get query params
        name = self.request.GET.get('name')
        # can change get to post to get post parameters
        # SELECT * FROM main_app_artist WHERE name=""
        if name != None:
            context['artists'] = Artist.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            # SELECT * FROM main_app_artist
            context['artists'] = Artist.objects.all()
            context['header'] = f"Trending Artist"

        return context
# unlimited arguements in **kwargs, like spread operator


# class Song:
#    def __init__(self, name, artist):
#        self.name = name
#        self.artist = artist
#
#
# songs = [
#    Song("Happy Inc", "Gorillaz"),
#    Song("That one fallout boy song", "Panic! At The Disco"),
#    Song("The Joji Song", "Joji"),
# ]


class SongList(TemplateView):
    template_name = 'song_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = songs

        return context


class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = 'artist_create.html'

    def get_success_url(self):
        return reverse("artist_detail", kwargs={'pk': self.object.pk})


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    # DetailView will expect <PK> from URL and fill in context with the model and set name to model name

# SELECT "fields" FROM "model" WHERE id =pk;


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = 'artist_update.html'

    def get_success_url(self):
        return reverse("artist_detail", kwargs={'pk': self.object.pk})

# GET POST


class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = '/artists/'


# def Home(request):
#    return render(request, "home.html")
#
#
# class Example(View):
#    def get(request):
#        return""
#
#    def post(request):
#        return ""
class SongCreate(View):
    def post(self, request, pk):
        title = request.POST.get('title')
        length = request.POST.get('length')
        artist = Artist.objects.get(pk=pk)
        Song.objects.create(title=title, length=length, artist=artist)
        return redirect('artist_detail', pk=pk)
