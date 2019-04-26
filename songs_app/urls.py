from django.urls import path
from . import views

app_name = 'songs_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('lyrics/', views.lyrics, name='lyrics'),
    path('random_song/', views.random_song, name='random_song'),
    path('top_songs/', views.top_songs, name='top_songs'),
    path('test/', views.test, name='test')
]
