from django.contrib.auth import logout
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from core.permissions import IsUserUpdate
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer, UpdateUserSerializer,\
    ProfileIdSerializer
from rest_framework import generics, permissions


class ProfileAllApiView(generics.ListCreateAPIView):
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


class RegisterApiView(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UpdateUserApiView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsUserUpdate, )


class LogoutApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response({'detail': "Успешно"})


# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer
#
#     def post(self, request, format=None):
#         data = request.data
#         username = data.get('username', None)
#         password = data.get('password', None)
#         user = authenticate(username=username, password=password)
#         if user is None:
#             raise exceptions.NotFound("Такого пользователя не существует")
#         if not user.check_password(password):
#             raise exceptions.NotFound("Не верный логин или пароль")
#         else:
#             login(request, user)
#             refresh = RefreshToken.for_user(user)
#             return Response({'access_token': str(refresh.access_token), 'refresh_token': str(
#                 refresh)})

