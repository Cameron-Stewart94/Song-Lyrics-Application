from django.urls import path
from . import views

app_name = 'songs_app'
# Sets app name to song's app so template tagging can be used

urlpatterns = [
    path('', views.index, name='index'),
    path('lyrics/', views.lyrics, name='lyrics'),
    path('random_song/', views.random_song, name='random_song'),
    path('top_songs/', views.top_songs, name='top_songs'),
]
