from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileSerializer(ModelSerializer):
    """ Сериалайзер для вывода всех пользователей"""
    class Meta:
        model = Profile
        fields = ['id', 'username', 'type_user', 'img', ]


class ProfileFullSerializer(ModelSerializer):
    """ Сериалайзер для регистрации """
    class Meta:
        model = Profile
        fields = ['id', 'username', 'type_user', 'img', 'password']


class ProfileMusicSerializer(ModelSerializer):
    """ Сериалайзер для отображения username в сериалайзере музыки"""
    class Meta:
        model = Profile
        fields = ['username', ]
