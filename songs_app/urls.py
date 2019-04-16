from django.urls import path
from . import views

app_name = 'songs_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('lyrics/', views.lyrics, name='lyrics')
]
