from django.contrib import admin
from .models import Music, Genre, Like, Playlist


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

