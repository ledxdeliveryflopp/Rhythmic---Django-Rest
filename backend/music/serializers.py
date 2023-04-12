from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Music, Albums, Genre
from user.serializers import ProfileMusicSerializer


class MusicTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Music
        fields = ['title']


class AlbumTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Albums
        fields = ['title']


class GenreSerializer(ModelSerializer):
    """ Сериалайрез списка жанров """

    class Meta:
        model = Genre
        fields = ['title']


class MusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    author = ProfileMusicSerializer(read_only=True)
    album = AlbumTestSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'genre', 'album', 'img', 'likes', ]


class AlbumSerializer(ModelSerializer):
    """ Сериалайрез альбомов """
    author = ProfileMusicSerializer(read_only=True)
    musics = MusicTestSerializer(read_only=True, many=True)

    class Meta:
        model = Albums
        fields = ['id', 'title', 'author', 'musics', 'img', 'likes', ]


class MusicListenSerializer(ModelSerializer):
    """ Сериалайрез прослушивания музыки """
    upload_by = ProfileMusicSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'img', 'likes', 'music_file', ]


class MusicCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания музыки"""

    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'album', 'music_file', ]


class MusicUpdateSerializer(ModelSerializer):
    """ Сериалайзер для обновления музыки"""
    class Meta:
        model = Music
        fields = ['id', 'title', 'genre', 'img', 'music_file']


class AlbumCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания альбома"""

    class Meta:
        model = Albums
        fields = ['id', 'title', 'img']


# class AlbumUpdateSerializer(ModelSerializer):
#     """ Сериалайзер для обновления альбома"""
#     title = serializers.CharField(required=False)
#     img = serializers.ImageField(required=False)
#
#     class Meta:
#         model = Albums
#         fields = ['title', 'tracks', 'img']