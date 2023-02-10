from rest_framework import generics, filters, permissions, authentication
from .models import Profile
from .serializers import ProfileSerializer, ProfileFullSerializer
from rest_framework import exceptions


class ProfileAPIView(generics.ListCreateAPIView):
    """ Получить информацию о всех пользователях """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class ProfileDetail(generics.RetrieveAPIView):
    """ Получить информацию о пользователе по его id """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreate(generics.CreateAPIView):
    """ Регистрация """
    queryset = Profile.objects.all()
    serializer_class = ProfileFullSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        """ Хэшируем пароль переопределяя метод из CreateModelMixin """
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


# class ExampleAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('username')
#         if not username:
#             return None
#
#         try:
#             user = Profile.objects.get(username=username)
#         except Profile.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         return user, None

