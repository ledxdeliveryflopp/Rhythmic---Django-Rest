from django.urls import path

from .views import MusicAPIView, MusicCreate

app_name = 'music'

urlpatterns = [
    path('all/', MusicAPIView.as_view(), name='Music-all'),
    path('create/',  MusicCreate.as_view(), name='Music-create'),
]
