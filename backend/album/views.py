from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.permissions import IsUserTypeTrue, IsUserOwner, IsUserUpdate
from .models import Album
from .serializers import AlbumSerializer, AlbumIDSerializer, AlbumCreateSerializer, \
    AlbumUpdateSerializer


class AlbumApiView(generics.ListCreateAPIView):
    """ Получить информацию о всех альбомах """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__username']
    permission_classes = (IsAuthenticated,)


class AlbumIdApiView(generics.RetrieveAPIView):
    """ Получить определенный альбом по ID """
    queryset = Album.objects.all()
    serializer_class = AlbumIDSerializer
    permission_classes = (IsAuthenticated,)


class AlbumCreateApiView(generics.CreateAPIView):
    """ Создание альбома """
    serializer_class = AlbumCreateSerializer
    permission_classes = (IsUserTypeTrue,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumDeleteApiView(generics.DestroyAPIView):
    """ Удаление альбома """
    queryset = Album.objects.all()
    serializer_class = AlbumIDSerializer
    permission_classes = (IsUserOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление успешно'})


class UpdateAlbumApiView(generics.UpdateAPIView):
    """Обновление альбома"""
    queryset = Album.objects.all()
    serializer_class = AlbumUpdateSerializer
    permission_classes = (IsUserUpdate, )
