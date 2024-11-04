from adminsortable2.admin import SortableAdminBase, SortableStackedInline, SortableAdminMixin

from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 1

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 150px; max-height: 150px;" />', self.image.url)
        return 'No Image'

    image_tag.short_description = 'Предпросмотр изображения'

    readonly_fields = ('image_tag',)
    fields = ('image', 'image_tag',)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('title',)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_number', 'image_tag', 'place')
    search_fields = ('place',)
    list_filter = ('place',)
    autocomplete_fields = ('place',)
