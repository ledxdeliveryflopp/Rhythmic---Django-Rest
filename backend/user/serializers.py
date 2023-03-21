from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileSerializer(ModelSerializer):
    """ Сериалайзер для вывода всех пользователей"""
    class Meta:
        model = Profile
        fields = ['id', 'username', 'type', 'img', ]


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
        fields = ['id', 'username', 'type', 'img', 'password', 'email']

class UpdateSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""

    class Meta:
        model = Profile
        fields = ['username', 'img', 'email']


class LoginSerializer(ModelSerializer):
    """ Сериалайзер для логина"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ['username', 'password']

