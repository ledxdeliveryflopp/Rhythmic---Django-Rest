from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.permissions import IsUserTypeTrue, IsUserOwner
from .models import Music, Genre
from .serializers import ALLMusicSerializer, MusicUpdateSerializer, MusicListenSerializer, \
    MusicCreateSerializer, GenreSerializer


class MusicAPIView(generics.ListAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = ALLMusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre__title', 'author__username']
    permission_classes = (IsAuthenticated,)


class GenreAPIView(generics.ListAPIView):
    """ Получить информацию о всех жанров """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)


class MusicListenApiView(generics.RetrieveAPIView):
    """ Получить определенный трек по ID """
    queryset = Music.objects.all()
    serializer_class = MusicListenSerializer
    permission_classes = (IsAuthenticated,)


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    serializer_class = MusicCreateSerializer
    permission_classes = (IsUserTypeTrue,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicUpdateSerializer
    permission_classes = (IsUserOwner,)


class MusicDelete(generics.DestroyAPIView):
    """ Удаление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicListenSerializer
    permission_classes = (IsUserOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Удаление успешно'})
