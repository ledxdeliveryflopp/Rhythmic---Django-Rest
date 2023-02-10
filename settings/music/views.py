from rest_framework import generics, filters
from .models import Music
from .serializers import MusicSerializer, MusicCreateSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre__title', 'upload_by__username', ]


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    queryset = Music.objects.all()
    serializer_class = MusicCreateSerializer

    def perform_create(self, serializer):
        serializer.save(upload_by=self.request.user)
