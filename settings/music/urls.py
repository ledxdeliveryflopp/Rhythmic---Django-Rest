from django.urls import path

from .views import MusicAPIView, MusicDetail, MusicCreate

app_name = 'music'

urlpatterns = [
    path('all/', MusicAPIView.as_view(), name='Music-all'),
    path('<int:pk>/', MusicDetail.as_view(), name='Music-detail'),
    path('create/', MusicCreate.as_view(), name='Music-create'),
]
