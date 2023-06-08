from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.permissions import IsUserOwner
from .models import Playlist
from .serializers import PlaylistSerializer, PlaylistCreateSerializer, PlaylistIdSerializer, \
    UpdatePlaylistSerializer


class PlaylistUserApiView(generics.ListAPIView):
    """ Получить информацию о плейлистах пользователя """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(author=user)


class PlaylistIDApiView(generics.RetrieveAPIView):
    """ Получить информацию о плейлисте пользователя """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistIdSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(author=user)


class PlaylistCreateApiView(generics.CreateAPIView):
    """ Создание плейлиста """
    serializer_class = PlaylistCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdatePlaylistApiView(generics.UpdateAPIView):
    """Обновление плейлиста"""
    queryset = Playlist.objects.all()
    serializer_class = UpdatePlaylistSerializer
    permission_classes = (IsUserOwner, )


class PlaylistDeleteApiView(generics.DestroyAPIView):
    """ Удаление плейлиста """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = (IsUserOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление успешно'})
