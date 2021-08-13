from main_app import views
from django.urls import path
from . import views
#from . (current dir) bring views
#path is like router router.get,router.post

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('about/',views.About.as_view(),name="about"),
    path('base/',views.Base.as_view(),name=('base')),
    path('artists/',views.ArtistList.as_view(),name='artist_list'),
    #as_view is a build in method n class Home to render file
]
