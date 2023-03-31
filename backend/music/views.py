from knox.auth import TokenAuthentication
from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Music
from .permissions import IsUserTypeTrue, IsUserOwner
from .serializers import MusicSerializer, MusicUpdateSerializer, MusicListenSerializer, MusicCreateSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'upload_by__username', ]
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
        serializer.save(upload_by=self.request.user)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicUpdateSerializer
    permission_classes = (IsUserOwner,)
    authentication_classes = (TokenAuthentication,)

