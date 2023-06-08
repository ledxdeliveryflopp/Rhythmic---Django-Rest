from django.contrib import admin
from .models import Favorite


@admin.register(Favorite)
class FavoriteeAdmin(admin.ModelAdmin):
    pass
