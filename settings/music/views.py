from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication

from .models import Music
from .serializers import MusicSerializer, MusicCreateSerializer, MusicDetailSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre__title', 'upload_by__username', ]


class MusicDetail(generics.RetrieveAPIView):
    """ Получить информацию о музыке по ее id """
    queryset = Music.objects.all()
    serializer_class = MusicDetailSerializer


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    queryset = Music.objects.all()
    serializer_class = MusicCreateSerializer

