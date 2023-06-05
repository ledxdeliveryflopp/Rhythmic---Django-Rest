from django.urls import path
from .views import MusicAPIView, MusicCreate, MusicUpdate, MusicListenApiView, GenreAPIView, \
    MusicDelete

app_name = 'music'

urlpatterns = [
    path('all-music/', MusicAPIView.as_view(), name='Music-all'),
    path('all-genre/', GenreAPIView.as_view(), name='Genre-all'),
    path('music<int:pk>/', MusicListenApiView.as_view(), name='music-listen'),
    path('create-music/',  MusicCreate.as_view(), name='Music-create'),
    path('update-music<int:pk>/',  MusicUpdate.as_view(), name='Music-update'),
    path('delete-music<int:pk>/',  MusicDelete.as_view(), name='Music-delete'),
]
