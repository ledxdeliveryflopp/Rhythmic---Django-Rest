from django.contrib import admin
from .models import Albums


@admin.register(Albums)
class AlbumAdmin(admin.ModelAdmin):
    pass

