from adminsortable2.admin import SortableAdminBase, SortableStackedInline, SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 1

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 150px; height: 150px;" />')
        return "No Image"

    image_tag.short_description = 'Image Preview'

    readonly_fields = ('image_tag',)
    fields = ('image', 'image_tag',)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ('title',)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'image_id', 'place')
    search_fields = ('image_id', 'place')
    list_filter = ('image_id', 'place')
