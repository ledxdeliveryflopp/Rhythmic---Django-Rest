from django.contrib.auth import logout
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from core.permissions import IsUserUpdate
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer, UpdateUserSerializer, \
    ProfileIdSerializer
from rest_framework import generics, permissions


class ProfileAllApiView(generics.ListAPIView):
    """ Получить информацию о всех пользователях """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = (IsAuthenticated,)


class ProfileIdDetailView(generics.RetrieveAPIView):
    """ Получить информацию о пользователе по его id """
    queryset = Profile.objects.all()
    serializer_class = ProfileIdSerializer
    permission_classes = (IsAuthenticated,)


class UpdateUserApiView(generics.UpdateAPIView):
    """Обновление пользователя"""
    queryset = Profile.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsUserUpdate, )


class RegisterApiView(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class LogoutApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response({'detail': "Успешно"})
