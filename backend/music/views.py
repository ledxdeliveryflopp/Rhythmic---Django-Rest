from knox.auth import TokenAuthentication
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Music, Albums, Genre
from .permissions import IsUserTypeTrue, IsUserTrackOwner
from .serializers import MusicSerializer, MusicUpdateSerializer, MusicListenSerializer, \
    MusicCreateSerializer, AlbumCreateSerializer, AlbumSerializer, GenreSerializer, \
    MusicTestSerializer, AlbumIDSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__username']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


# class MusicUrlAPIView(generics.ListCreateAPIView):
#     """ Получить url трека в альбоме """
#     queryset = Music.objects.all()
#     serializer_class = MusicTestSerializer


class GenreAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех жанров """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class MusicListenAPIView(generics.RetrieveAPIView):
    """ Получить определенный трек по ID """
    queryset = Music.objects.all()
    serializer_class = MusicListenSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class AlbumAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех альбомах """
    queryset = Albums.objects.all().order_by('-likes')
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__username']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class AlbumIDAPIView(generics.RetrieveAPIView):
    """ Получить определенный альбом по ID """
    queryset = Albums.objects.all()
    serializer_class = AlbumIDSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    serializer_class = MusicCreateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicUpdateSerializer
    permission_classes = (IsUserTrackOwner,)
    authentication_classes = (TokenAuthentication,)


class AlbumCreate(generics.CreateAPIView):
    """ Создание альбома """
    serializer_class = AlbumCreateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
