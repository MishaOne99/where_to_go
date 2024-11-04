from adminsortable2.admin import SortableAdminBase, SortableStackedInline, SortableAdminMixin

from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 1

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height: 150px;" />', self.image.url)
        return "No Image"

    image_tag.short_description = 'Image Preview'

    readonly_fields = ('image_tag',)
    fields = ('image', 'image_tag',)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'image_number', 'place')
    search_fields = ('image_number', 'place')
    list_filter = ('image_number', 'place')
