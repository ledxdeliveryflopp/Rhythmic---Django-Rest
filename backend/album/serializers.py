from rest_framework.serializers import ModelSerializer
from music.models import Music
from .models import Album
from user.serializers import ProfileMusicSerializer


class IDMusicAlbumSerializer(ModelSerializer):
    """ Сериалайзер для отображения id, title, music_file в сериалайзере альбома по ID"""

    class Meta:
        model = Music
        fields = ['id', 'title', 'music_file']


class IDAlbumMusicSerializer(ModelSerializer):
    """ Сериалайзер для отображения id в сериалайзере альбомов"""
    class Meta:
        model = Album
        fields = ['id']


class AlbumSerializer(ModelSerializer):
    """ Сериалайрез альбомов """
    author = ProfileMusicSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'author', 'img', 'likes']


class AlbumIDSerializer(ModelSerializer):
    """ Сериалайрез альбома по ID """
    author = ProfileMusicSerializer(read_only=True)
    musics = IDMusicAlbumSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'author', 'img', 'musics', 'likes']


class AlbumCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания альбома"""

    class Meta:
        model = Album
        fields = ['id', 'title', 'img']
