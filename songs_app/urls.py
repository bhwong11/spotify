from main_app import views
from django.urls import path
from . import views
#from . (current dir) bring views
#path is like router router.get,router.post

urlpatterns=[
    path('',views.SongList.as_view(),name='songs_list')
    #as_view is a build in method n class Home to render file
]