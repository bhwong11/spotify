from main_app import views
from django.urls import path
from .views import HomePage, About, Base, ArtistList, ArtistCreate, ArtistUpdate, ArtistDelete, ArtistDetail, SongCreate
# from . (current dir) bring views
# path is like router router.get,router.post

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('base/', Base.as_view(), name=('base')),
    path('artists/', ArtistList.as_view(), name='artist_list'),
    # as_view is a build in method n class Home to render file
    path('artists/new/', ArtistCreate.as_view(), name='artist_create'),
    path('artists/<int:pk>/update/',
         ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete/',
         ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/songs/new/', SongCreate.as_view(), name='song_create')
]
# '/products/:id = artist/<pk>
# int will pass it in as a number
# slug a unique name in url that is connected to a databse that can be used a replacement to the url, name-url
