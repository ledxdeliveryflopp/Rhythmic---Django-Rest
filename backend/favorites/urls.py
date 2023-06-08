from django.urls import path
from favorites.views import FavoriteUserApiView, UpdateFavoriteApiView

app_name = 'favorites'

urlpatterns = [
    path('my-favorites/', FavoriteUserApiView.as_view(), name='my-favorites'),
    path('my-favorites-update<int:pk>/',  UpdateFavoriteApiView.as_view(), name='Favorite-update'),
]
