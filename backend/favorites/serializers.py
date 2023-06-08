from rest_framework.serializers import ModelSerializer
from .models import Favorite


class UserFavoriteSerializer(ModelSerializer):
    """ Сериалайзер для вывода избранного пользователя"""

    class Meta:
        model = Favorite
        fields = ['title', 'music']


class UpdateFavoriteSerializer(ModelSerializer):
    """ Сериалайзер для обновления избранного"""

    class Meta:
        model = Favorite
        fields = ['music']
