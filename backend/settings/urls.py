from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('music.urls', namespace='music')),
    path('api/', include('album.urls', namespace='album')),
    path('api/', include('user.urls', namespace='user')),
    path('api/', include('playlist.urls', namespace='playlist')),
]
