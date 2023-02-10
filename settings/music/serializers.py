from rest_framework.serializers import ModelSerializer
from .models import Music, Genre

from user.serializers import ProfileMusicSerializer


class GenreSerializer(ModelSerializer):
    """ Сериалайрез жанра для сериалайзера музыки"""

    class Meta:
        model = Genre
        fields = ['title', ]


class MusicSerializer(ModelSerializer):
    """ Сериалайрез музыки на главной странице"""
    upload_by = ProfileMusicSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'upload_by', 'genre', 'img', 'likes', ]


class MusicDetailSerializer(ModelSerializer):
    """ Сериалайрез музыки на странице музыки"""
    upload_by = ProfileMusicSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'upload_by', 'genre', 'img', 'music_file', ]


class MusicCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания музыки"""

    class Meta:
        model = Music
        fields = '__all__'

