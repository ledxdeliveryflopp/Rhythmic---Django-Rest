from django.contrib import admin
from .models import Music, Album


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
