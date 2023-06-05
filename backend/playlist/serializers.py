from rest_framework.serializers import ModelSerializer
from music.models import Music
from .models import Playlist
from user.serializers import ProfileMusicSerializer


class IdMusicPlaylistSerializer(ModelSerializer):
    """ Сериалайзер для отображения id, title, img, music_file в сериалайзере плейлистов """

    class Meta:
        model = Music
        fields = ['id', 'title', 'img', 'music_file']


class PlaylistSerializer(ModelSerializer):
    """ Сериалайрез плейлистов """
    author = ProfileMusicSerializer(read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'title', 'author', 'img', 'music']


class PlaylistIdSerializer(ModelSerializer):
    """ Сериалайрез плейлистов """
    author = ProfileMusicSerializer(read_only=True)
    music = IdMusicPlaylistSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ['id', 'title', 'author', 'img', 'music']


class PlaylistCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания плейлиста"""

    class Meta:
        model = Playlist
        fields = ['title', 'img', 'music']


class UpdatePlaylistSerializer(ModelSerializer):
    """ Сериалайзер для обновления плейлиста"""

    class Meta:
        model = Playlist
        fields = ['title', 'img', 'music']
