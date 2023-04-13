from rest_framework.serializers import ModelSerializer
from album.serializers import IDAlbumMusicSerializer
from .models import Music, Genre
from user.serializers import ProfileMusicSerializer


class GenreSerializer(ModelSerializer):
    """ Сериалайрез списка жанров """

    class Meta:
        model = Genre
        fields = ['id', 'title']


class ALLMusicSerializer(ModelSerializer):
    """ Сериалайрез музыки """
    author = ProfileMusicSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    # album = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='music:album-view'
    # )
    album = IDAlbumMusicSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'title', 'author', 'genre', 'album', 'img', 'likes', ]


class MusicListenSerializer(ModelSerializer):
    """ Сериалайрез прослушивания музыки """
    author = ProfileMusicSerializer(read_only=True)
    album = IDAlbumMusicSerializer(read_only=True)

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

