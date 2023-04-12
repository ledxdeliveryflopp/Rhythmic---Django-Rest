from django.urls import path

from .views import MusicAPIView, MusicCreate, MusicUpdate, MusicListenAPIView, AlbumCreate, \
    AlbumAPIView, GenreAPIView

app_name = 'music'

urlpatterns = [
    path('all-music/', MusicAPIView.as_view(), name='Music-all'),
    path('all-genre/', GenreAPIView.as_view(), name='Genre-all'),
    path('all-album/', AlbumAPIView.as_view(), name='Album-all'),
    path('music<int:pk>/', MusicListenAPIView.as_view(), name='music-listen'),
    path('create-music/',  MusicCreate.as_view(), name='Music-create'),
    path('create-album/',  AlbumCreate.as_view(), name='Album-create'),
    path('update-music<int:pk>/',  MusicUpdate.as_view(), name='Music-update'),
    # path('update-album<int:pk>/',  AlbumUpdate.as_view(), name='Album-update'),
]
