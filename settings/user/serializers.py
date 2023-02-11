from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileSerializer(ModelSerializer):
    """ Сериалайзер для вывода всех пользователей"""
    class Meta:
        model = Profile
        fields = ['id', 'username', 'type_user', 'img', ]


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
        fields = ['id', 'username', 'type_user', 'img', 'password', 'email']


class LoginSerializer(ModelSerializer):
    """ Сериалайзер для логина"""

    class Meta:
        model = Profile
        fields = ('id', 'username', 'password')
        password = CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError('Не верные данные')
