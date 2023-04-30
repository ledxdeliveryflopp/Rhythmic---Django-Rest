from django.contrib import admin
from .models import Music, Genre


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

