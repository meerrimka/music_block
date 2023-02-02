
from django.contrib import admin
from django.urls import path
# from music.views import get_hello
# from music.views import get_musics
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', get_hello),
    path('music/', get_musics),
    path('music/<int:id>', get_song),
    path('music/create/', post_musics),
]
