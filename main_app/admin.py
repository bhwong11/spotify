from django.contrib import admin
from .models import Artist, Song

# Register your models here.

# this will give you access to the artist.model in the admin page
admin.site.register(Artist)
admin.site.register(Song)
