from rest_framework import serializers
from music.models import Music


class MusicSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'