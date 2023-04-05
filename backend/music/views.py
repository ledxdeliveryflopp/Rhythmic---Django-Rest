from knox.auth import TokenAuthentication
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Music, Album
from .permissions import IsUserTypeTrue, IsUserTrackOwner, IsUserAlbumOwner
from .serializers import MusicSerializer, MusicUpdateSerializer, MusicListenSerializer, \
    MusicCreateSerializer, AlbumSerializer, AlbumCreateSerializer, AlbumUpdateSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__username']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class AlbumAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех альбомах """
    queryset = Album.objects.all().order_by('-likes')
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__username']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class MusicListenAPIView(generics.RetrieveAPIView):
    """ Получить определенный трек по ID """
    queryset = Music.objects.all()
    serializer_class = MusicListenSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    serializer_class = MusicCreateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumCreate(generics.CreateAPIView):
    """ Создание альбома """
    serializer_class = AlbumCreateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (TokenAuthentication,)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    #     serializer.save(tracks=self.request.tracks)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicUpdateSerializer
    permission_classes = (IsUserTrackOwner,)
    authentication_classes = (TokenAuthentication,)


class AlbumUpdate(generics.UpdateAPIView):
    """ Обновление альбома """
    queryset = Album.objects.all()
    serializer_class = AlbumUpdateSerializer
    permission_classes = (IsUserAlbumOwner,)
    authentication_classes = (TokenAuthentication,)


