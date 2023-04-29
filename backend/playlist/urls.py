from django.urls import path
from .views import PlaylistCreate, PlaylistAPIView

app_name = 'playlist'

urlpatterns = [
    path('create-playlist/',  PlaylistCreate.as_view(), name='Playlist-create'),
    path('playlist/',  PlaylistAPIView.as_view(), name='Playlist'),
]
