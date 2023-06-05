from django.contrib.auth import login, logout, authenticate
from rest_framework import filters, exceptions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer, LoginSerializer, UpdateSerializer, ProfileIDSerializer
from rest_framework import generics, permissions
from .permissions import IsUserUpdate


class ProfileAllAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех пользователях """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = (permissions.IsAuthenticated,)


class ProfileDetail(generics.RetrieveAPIView):
    """ Получить информацию о пользователе по его id """
    queryset = Profile.objects.all()
    serializer_class = ProfileIDSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RegisterAPI(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UpdateUserAPI(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (IsUserUpdate, )


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response({'detail': "Успешно"})


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise exceptions.NotFound("Такого пользователя не существует")
        if not user.check_password(password):
            raise exceptions.NotFound("Не верный логин или пароль")
        else:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({'access_token': str(refresh.access_token), 'refresh_token': str(
                refresh)})

