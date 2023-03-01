from django.urls import path
from .views import ProfileAllAPIView, ProfileDetail, RegisterAPI, LoginAPI, UpdateUserAPI
from knox import views as knox_views

app_name = 'user'

urlpatterns = [
    path('all/', ProfileAllAPIView.as_view(), name='profile-all'),
    path('User<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('register/', RegisterAPI.as_view(), name='profile-create'),
    path('update-user<int:pk>/', UpdateUserAPI.as_view(), name='profile-create'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logout_all'),
]
