from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsUserOwner
from .models import Favorite
from .serializers import UserFavoriteSerializer, UpdateFavoriteSerializer


class FavoriteUserApiView(generics.ListAPIView):
    """ Получить информацию о избранном пользователя """
    queryset = Favorite.objects.all()
    serializer_class = UserFavoriteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(author=user)


class UpdateFavoriteApiView(generics.UpdateAPIView):
    """Обновление избранного"""
    queryset = Favorite.objects.all()
    serializer_class = UpdateFavoriteSerializer
    permission_classes = (IsUserOwner, )
