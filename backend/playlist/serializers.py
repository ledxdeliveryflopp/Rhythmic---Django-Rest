from rest_framework.serializers import ModelSerializer
from music.models import Music
from .models import Playlist
from user.serializers import ProfileMusicSerializer


class IDMusicPlaylistSerializer(ModelSerializer):
    """ Сериалайзер для отображения id, title, music_file в сериалайзере плейлистов """

    class Meta:
        model = Music
        fields = ['id', 'title', 'music_file']


class PlaylistSerializer(ModelSerializer):
    """ Сериалайрез плейлистов """
    author = ProfileMusicSerializer(read_only=True)
    musics = IDMusicPlaylistSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ['id', 'title', 'author', 'musics']


class PlaylistCreateSerializer(ModelSerializer):
    """ Сериалайзер для создания плейлиста"""

    class Meta:
        model = Playlist
        fields = ['title', 'musics']
