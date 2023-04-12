from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Music, Albums, Genre
from user.serializers import ProfileMusicSerializer


class MusicTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Music
        fields = ['title']


class MusicFileSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Music
        fields = ['id', 'title', 'music_file']


class AlbumTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Albums
        fields = ['id']


class GenreSerializer(ModelSerializer):
    """ Сериалайрез списка жанров """

    class Meta:
        model = Genre
        fields = ['title']


class MusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    author = ProfileMusicSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    # album = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='music:album-view'
    # )
    album = AlbumTestSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'genre', 'album', 'img', 'likes', ]


class AlbumSerializer(ModelSerializer):
    """ Сериалайрез альбомов """
    author = ProfileMusicSerializer(read_only=True)

    class Meta:
        model = Albums
        fields = ['id', 'title', 'author', 'img', 'likes']


class AlbumIDSerializer(ModelSerializer):
    """ Сериалайрез альбома по ID """
    author = ProfileMusicSerializer(read_only=True)
    musics = MusicFileSerializer(many=True)

    class Meta:
        model = Albums
        fields = ['id', 'title', 'author', 'img', 'musics', 'likes']


class MusicListenSerializer(ModelSerializer):
    """ Сериалайрез прослушивания музыки """
    author = ProfileMusicSerializer(read_only=True)
    album = AlbumTestSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'img', 'album', 'likes', 'music_file', ]


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
