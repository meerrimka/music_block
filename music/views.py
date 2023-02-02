from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSeriallizer

@api_view(['GET'])
def get_hello(request):
    return Response('True')


@api_view(['GET'])
def get_musics(requests):
    musics = Music.objects.all()
    serializer = MusicSeriallizer(musics, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_song(requests, id):
    song = Music.objects.get(id=id)
    serializer = MusicSeriallizer(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def post_musics(requests):
    # print(requests.data)
    serializer = MusicSeriallizer(data=requests.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
