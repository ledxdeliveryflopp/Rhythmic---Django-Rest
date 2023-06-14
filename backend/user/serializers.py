from typing import List
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from music.models import Music
from .models import Profile


class UserMusicSerializer(ModelSerializer):
    """ Сериалайзер для отображения id, title в сериалайзере юзера"""

    class Meta:
        model = Music
        fields = ['id', 'title']


class MusicTestSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Music
        fields = ['title']


class ProfileSerializer(ModelSerializer):
    """ Сериалайзер для вывода всех пользователей"""

    class Meta:
        model = Profile
        fields = ['id', 'username', 'type_user', 'img']


class ProfileIdSerializer(ModelSerializer):
    """ Сериалайзер для вывода пользователя по ID"""
    musics = UserMusicSerializer(many=True)

    class Meta:
        model = Profile
        fields: List = ['id', 'username', 'musics', 'playlist', 'favorite', 'type_user', 'img']


class ProfileMusicSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Profile
        fields = ['username', ]


class RegisterSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'type_user', 'img', 'password']


class UpdateUserSerializer(ModelSerializer):
    """ Сериалайзер для обновления пользователя"""

    class Meta:
        model = Profile
        fields = ['username', 'img']


class LoginSerializer(ModelSerializer):
    """ Сериалайзер для логина"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['username', 'password']
