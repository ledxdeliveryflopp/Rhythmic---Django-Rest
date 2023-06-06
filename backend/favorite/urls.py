from django.urls import path
from favorite.views import AddFavoriteMusicApi, ChangeFavoriteMusicApi, FavoriteUserMusicApi

app_name = 'favorite'

urlpatterns = [
    path('favorite/', FavoriteUserMusicApi.as_view(), name='favorite'),
    path('add-favorite/', AddFavoriteMusicApi.as_view(), name='favorite-add'),
    path('add-favorite-music<int:pk>/', ChangeFavoriteMusicApi.as_view(), name='favorite-add-music'),
]
