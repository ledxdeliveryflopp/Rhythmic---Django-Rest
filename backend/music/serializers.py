from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Music, Album
from user.serializers import ProfileMusicSerializer


class MusicTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Music
        fields = ['title']


class AlbumTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Album
        fields = ['title']


class MusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    author = ProfileMusicSerializer(read_only=True)
    album = AlbumTestSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'genre', 'album', 'img', 'likes', ]


class AlbumSerializer(ModelSerializer):
    """ Сериалайрез альбомов """
    author = ProfileMusicSerializer(read_only=True)
    tracks = MusicTestSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'author', 'tracks', 'img', 'likes', ]


class MusicListenSerializer(ModelSerializer):
    """ Сериалайрез прослушивания музыки """
    upload_by = ProfileMusicSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'img', 'likes', 'music_file', ]


class MusicCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания музыки"""
    album = AlbumTestSerializer(many=True, required=False)

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
    tracks = MusicTestSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = ['id', 'title', 'tracks', 'img']


class AlbumUpdateSerializer(ModelSerializer):
    """ Сериалайзер для обновления альбома"""
    title = serializers.CharField(required=False)
    img = serializers.ImageField(required=False)

    class Meta:
        model = Album
        fields = ['title', 'tracks', 'img']

