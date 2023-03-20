from knox.auth import TokenAuthentication
from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Music
from .permissions import IsUserTypeTrue, IsUserOwner
from .serializers import MusicSerializer, MusicCreateUpdateSerializer


class MusicAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всей музыке """
    queryset = Music.objects.all().order_by('-likes')
    serializer_class = MusicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre__title', 'upload_by__username', ]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class MusicCreate(generics.CreateAPIView):
    """ Создание музыки """
    serializer_class = MusicCreateUpdateSerializer
    permission_classes = (IsUserTypeTrue,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(upload_by=self.request.user)


class MusicUpdate(generics.UpdateAPIView):
    """ Обновление музыки """
    queryset = Music.objects.all()
    serializer_class = MusicCreateUpdateSerializer
    permission_classes = (IsUserOwner,)
    authentication_classes = (TokenAuthentication,)

    def patch(self, *args, **kwargs):
        # Получаем объект
        instance = Music.objects.get(pk=kwargs.get('pk'))
        # Получаем из запроса наш файл
        instance.img = self.request.FILES['img']
        instance.music_file = self.request.FILES['music_file']
        # Сохраняем запись
        instance.save()
        # Возвращаем ответ
        return Response(
            MusicCreateUpdateSerializer(instance).data,
            status=status.HTTP_200_OK
        )
