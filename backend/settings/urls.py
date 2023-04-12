from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('music.urls', namespace='music')),
    path('api/', include('album.urls', namespace='album')),
    path('api/', include('user.urls', namespace='user')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
