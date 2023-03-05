from rest_framework.serializers import ModelSerializer
from .models import Music, Genre

from user.serializers import ProfileMusicSerializer


class GenreSerializer(ModelSerializer):
    """ Сериалайрез жанра для сериалайзера музыки"""

    class Meta:
        model = Genre
        fields = ['title', ]


class MusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    upload_by = ProfileMusicSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'upload_by', 'genre', 'img', 'likes', 'music_file', ]


class MusicCreateUpdateSerializer(ModelSerializer):
    """ Сериалайзер для обновления музыки"""

    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'music_file', ]


# authentication_classes = [TokenAuthentication]