from django.urls import path
from .views import ProfileAPIView, ProfileDetail, ProfileCreate

app_name = 'user'

urlpatterns = [
    path('all/', ProfileAPIView.as_view(), name='profile-all'),
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('create/', ProfileCreate.as_view(), name='profile-create'),
]
