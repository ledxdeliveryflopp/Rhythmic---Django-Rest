from knox.auth import TokenAuthentication
from rest_framework import generics, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Playlist
from .serializers import PlaylistSerializer, PlaylistCreateSerializer


class PlaylistAPIView(generics.ListCreateAPIView):
    """ Получить информацию о плейлистах пользователя """
    serializer_class = PlaylistSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(author=user)


class PlaylistCreate(generics.CreateAPIView):
    """ Создание плейлиста """
    serializer_class = PlaylistCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
