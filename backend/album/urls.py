from django.urls import path
from .views import AlbumAPIView, AlbumIDAPIView, AlbumCreate

app_name = 'album'

urlpatterns = [
    path('all-album/', AlbumAPIView.as_view(), name='Album-all'),
    path('album<int:pk>/', AlbumIDAPIView.as_view(), name='album-view'),
    path('create-album/',  AlbumCreate.as_view(), name='Album-create'),
]
