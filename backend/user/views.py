from django.contrib.auth import login, logout, authenticate
from knox.auth import TokenAuthentication
from pytz import unicode
from rest_framework import filters, exceptions, authentication, response, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer, LoginSerializer, UpdateSerializer, ProfileIDSerializer
from rest_framework import generics, permissions
from knox.views import LoginView as KnoxLoginView
from .permissions import IsUserUpdate


class ProfileAllAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех пользователях """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class ProfileDetail(generics.RetrieveAPIView):
    """ Получить информацию о пользователе по его id """
    queryset = Profile.objects.all()
    serializer_class = ProfileIDSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


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
    authentication_classes = (SessionAuthentication,)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        logout(request)
        return Response()


# class MyBasicAuthentication(BasicAuthentication):
#
#     def authenticate(self, request):
#         user, _ = super(MyBasicAuthentication, self).authenticate(request)
#         login(request, user)
#         return user, _
#
#
# class ExampleView(APIView):
#     authentication_classes = (SessionAuthentication, MyBasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, format=None):
#         content = {
#             'user':  unicode(request.user),
#         }
#         return Response(content)

# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     # renderer_classes = (UserJSONRenderer,)
#     serializer_class = LoginSerializer
#
#     def post(self, request):
#         user = request.data.get('user', {})
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class LoginAPI(APIView):
#     permission_classes = (permissions.AllowAny,)
#     # serializer_class = LoginSerializer
#
#     def post(self, request, format=None):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
