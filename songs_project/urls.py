from django.contrib import admin
from django.urls import path, include
from songs_app import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
    path('songs_app/', include('songs_app.urls', namespace='songs_app')),
]
