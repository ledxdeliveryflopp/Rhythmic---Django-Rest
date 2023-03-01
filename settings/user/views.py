from django.contrib.auth import login
from rest_framework import filters, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer, LoginSerializer, UpdateSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .permissions import IsUserUpdate


class ProfileAllAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех пользователях """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = (permissions.AllowAny,)


class ProfileDetail(generics.RetrieveAPIView):
    """ Получить информацию о пользователе по его id """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


class RegisterAPI(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response({
            "user": ProfileSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UpdateUserAPI(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateSerializer
    permissions_classes = (IsUserUpdate, )

    def patch(self, request, *args, **kwargs):
        instance = request.user.get
        instance.img = self.request.files['img']
        instance.save()
        return Response(
            UpdateSerializer(instance).data,
            status=status.HTTP_200_OK
        )


class LoginAPI(KnoxLoginView):
    """ Вход """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
