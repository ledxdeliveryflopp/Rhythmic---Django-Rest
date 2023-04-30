from django.urls import path
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
    # path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]
