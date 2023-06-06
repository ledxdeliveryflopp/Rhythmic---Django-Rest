from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from favorite.models import Favorite


class FavoriteMusicUserSerializer(ModelSerializer):
    """Сериалайзер для вывода избранной музыки"""

    class Meta:
        model = Favorite
        fields = '__all__'


class AddFavoriteMusicSerializer(ModelSerializer):
    """Сериалайзер для добавления избранного"""

    class Meta:
        model = Favorite
        fields = ['music']


class ChangeFavoriteMusicSerializer(ModelSerializer):
    """Сериалайзер для добавления в избранное"""

    class Meta:
        model = Favorite
        fields = ['music']
