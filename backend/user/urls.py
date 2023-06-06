from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import ProfileAllApiView, ProfileIdDetailView, RegisterApiView, UpdateUserApiView, \
    LogoutApiView

app_name = 'user'

urlpatterns = [
    path('all/', ProfileAllApiView.as_view(), name='profile-all'),
    path('user<int:pk>/', ProfileIdDetailView.as_view(), name='profile-detail'),
    path('register/', RegisterApiView.as_view(), name='profile-create'),
    path('update-user<int:pk>/', UpdateUserApiView.as_view(), name='profile-create'),
    # path('login/', LoginAPIView.as_view(), name='login'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('logout/', LogoutApiView.as_view(), name='logout'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
