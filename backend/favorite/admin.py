from django.contrib import admin
from favorite.models import Favorite


@admin.register(Favorite)
class ProfileFavorite(admin.ModelAdmin):
    pass
