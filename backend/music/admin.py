from django.contrib import admin
from .models import Music, Albums, Genre


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Albums)
class AlbumAdmin(admin.ModelAdmin):
    pass
