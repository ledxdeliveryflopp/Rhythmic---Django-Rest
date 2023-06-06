from rest_framework.serializers import ModelSerializer
from album.serializers import IDAlbumMusicSerializer
from .models import Music, Genre
from user.serializers import ProfileMusicSerializer


class GenreSerializer(ModelSerializer):
    """ Сериалайрез списка жанров """

    class Meta:
        model = Genre
        fields = ['id', 'title']


# class LikeSerializer(ModelSerializer):
#     """ Сериалайрез списка жанров """
#
#     class Meta:
#         model = Like
#         fields = ['title']


class ALLMusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    author = ProfileMusicSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    album = IDAlbumMusicSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'genre', 'album', 'likes', 'img']


class MusicListenSerializer(ModelSerializer):
    """ Сериалайрез прослушивания музыки """
    author = ProfileMusicSerializer(read_only=True)
    album = IDAlbumMusicSerializer(read_only=True)

    class Meta:
        model = Music
        fields = '__all__'


class MusicCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания музыки"""

    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'album', 'music_file']


class MusicUpdateSerializer(ModelSerializer):
    """ Сериалайзер для обновления музыки"""
    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'music_file']

