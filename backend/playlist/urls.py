from django.urls import path
from .views import PlaylistCreateApiView, PlaylistUserApiView, PlaylistIDApiView, \
    PlaylistDeleteApiView, UpdatePlaylistApiView

app_name = 'playlist'

urlpatterns = [
    path('create-playlist/',  PlaylistCreateApiView.as_view(), name='Playlist-create'),
    path('all-user-playlist/',  PlaylistUserApiView.as_view(), name='Playlist'),
    path('playlist<int:pk>/',  PlaylistIDApiView.as_view(), name='Playlist-id'),
    path('playlist-delete<int:pk>/',  PlaylistDeleteApiView.as_view(), name='Playlist-delete'),
    path('playlist-update<int:pk>/',  UpdatePlaylistApiView.as_view(), name='Playlist-update'),
]
