from django.contrib import admin

from .models import Place, Image


class PlaceElementInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceElementInline]

admin.site.register(Image)
