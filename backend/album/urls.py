from django.urls import path
from .views import AlbumApiView, AlbumIdApiView, AlbumCreateApiView, AlbumDeleteApiView, \
    UpdateAlbumApiView

app_name = 'album'

urlpatterns = [
    path('all-album/', AlbumApiView.as_view(), name='Album-all'),
    path('album<int:pk>/', AlbumIdApiView.as_view(), name='album-id'),
    path('create-album/',  AlbumCreateApiView.as_view(), name='Album-create'),
    path('delete-album<int:pk>/',  AlbumDeleteApiView.as_view(), name='Album-delete'),
    path('update-album<int:pk>/',  UpdateAlbumApiView.as_view(), name='Album-update'),
]
