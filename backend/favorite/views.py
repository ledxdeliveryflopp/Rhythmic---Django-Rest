from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Favorite
from .serializers import AddFavoriteMusicSerializer, ChangeFavoriteMusicSerializer, \
    FavoriteMusicUserSerializer


class FavoriteUserMusicApi(generics.ListAPIView):
    """Вывод избранной музыки пользователя"""
    serializer_class = FavoriteMusicUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # user = self.request.user
        return Favorite.objects.filter(author=self.request.user)


class AddFavoriteMusicApi(generics.CreateAPIView):
    """Создание избранного"""
    queryset = Favorite.objects.all()
    serializer_class = AddFavoriteMusicSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # if Favorite.objects.get(author=self.request.user):
        #     return Response({'detail': 'У пользователя есть избранное'})
        # else:
        return serializer.save(author=self.request.user)


class ChangeFavoriteMusicApi(generics.UpdateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = ChangeFavoriteMusicSerializer
    permission_classes = (IsAuthenticated,)
