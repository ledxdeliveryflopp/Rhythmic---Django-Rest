from rest_framework import generics, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsUserTypeTrue, IsUserTrackOwner
from .models import Music, Genre
from .serializers import ALLMusicSerializer, MusicUpdateSerializer, MusicListenSerializer, \
    MusicCreateSerializer, GenreSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = ALLMusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__username']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class GenreAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех жанров """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class MusicListenAPIView(generics.RetrieveAPIView):
    """ Получить определенный трек по ID """
    queryset = Music.objects.all()
    serializer_class = MusicListenSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    serializer_class = MusicCreateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (SessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicUpdateSerializer
    permission_classes = (IsUserTrackOwner,)
    authentication_classes = (SessionAuthentication,)


# class MusicAddLike(generics.UpdateAPIView):
#     """ Добавление лайков """
#     queryset = Music.objects.all()
#     serializer_class = MusicUpdateSerializer
#     authentication_classes = (SessionAuthentication,)

