from main_app import views
from django.urls import path
from . import views
# from . (current dir) bring views
# path is like router router.get,router.post

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('base/', views.Base.as_view(), name=('base')),
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    # as_view is a build in method n class Home to render file
    path('artists/new/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artists/<int:pk>/update/',
         views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),

]
# '/products/:id = artist/<pk>
# int will pass it in as a number
# slug a unique name in url that is connected to a databse that can be used a replacement to the url, name-url
