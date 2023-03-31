from rest_framework.serializers import ModelSerializer
from .models import Music
from user.serializers import ProfileMusicSerializer


class MusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    upload_by = ProfileMusicSerializer(read_only=True)
    # genre = GenreSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'upload_by', 'genre', 'img', 'likes', ]


class MusicListenSerializer(ModelSerializer):
    """ Сериалайрез прослушивания музыки """
    upload_by = ProfileMusicSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'upload_by', 'img', 'likes', 'music_file', ]


class MusicCreateSerializer(ModelSerializer):
    """ Сериалайзер для обновления-создания музыки"""

    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'music_file', ]


class MusicUpdateSerializer(ModelSerializer):
    """ Сериалайзер для обновления-создания музыки"""
    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'music_file', ]
