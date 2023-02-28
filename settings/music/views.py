from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Music
from .permissions import IsUserTypeTrue
from .serializers import MusicSerializer, MusicCreateUpdateSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre__title', 'upload_by__username', ]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    serializer_class = MusicCreateUpdateSerializer
    permission_classes = (IsUserTypeTrue,)

    def perform_create(self, serializer):
        serializer.save(upload_by=self.request.user)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    serializer_class = MusicCreateUpdateSerializer
    permission_classes = (IsUserTypeTrue,)

    def perform_create(self, serializer):
        serializer.save(upload_by=self.request.user)