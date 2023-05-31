from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import ProfileAllAPIView, ProfileDetail, RegisterAPI, UpdateUserAPI, Logout, \
    LoginAPIView

app_name = 'user'

urlpatterns = [
    path('all/', ProfileAllAPIView.as_view(), name='profile-all'),
    path('user<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('register/', RegisterAPI.as_view(), name='profile-create'),
    path('update-user<int:pk>/', UpdateUserAPI.as_view(), name='profile-create'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
