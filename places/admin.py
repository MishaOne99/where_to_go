from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class PlaceElementInline(admin.TabularInline):
    model = Image
    
    fields = ('image', 'preview', 'image_id')
    readonly_fields = ['preview']
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 150px;">')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceElementInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
