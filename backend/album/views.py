from knox.auth import TokenAuthentication
from rest_framework import generics, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsUserTypeTrue
from .models import Album
from .serializers import AlbumSerializer, AlbumIDSerializer, AlbumCreateSerializer


class AlbumAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех альбомах """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__username']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class AlbumIDAPIView(generics.RetrieveAPIView):
    """ Получить определенный альбом по ID """
    queryset = Album.objects.all()
    serializer_class = AlbumIDSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class AlbumCreate(generics.CreateAPIView):
    """ Создание альбома """
    serializer_class = AlbumCreateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (SessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
