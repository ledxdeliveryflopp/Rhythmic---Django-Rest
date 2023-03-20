from django.urls import path

from .views import MusicAPIView, MusicCreate, MusicUpdate, MusicListenAPIView

app_name = 'music'

urlpatterns = [
    path('all-music/', MusicAPIView.as_view(), name='Music-all'),
    path('music<int:pk>/', MusicListenAPIView.as_view(), name='music-listen'),
    path('create-music/',  MusicCreate.as_view(), name='Music-create'),
    path('update-music<int:pk>/',  MusicUpdate.as_view(), name='Music-update'),
]
