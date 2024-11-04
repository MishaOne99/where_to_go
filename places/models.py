from django.db import models
from django.utils.safestring import mark_safe

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    long_description = HTMLField(blank=True, verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
    
    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Название локации', related_name='images')
    image = models.ImageField(verbose_name='Изображение')
    image_id = models.PositiveIntegerField(db_index=True, default=1, verbose_name='Номер изображения')
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        
        ordering = ['image_id']
    
    def __str__(self) -> str:
        return str(self.place)
    
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 150px; height: 150px;" />')
        return "No Image"

    image_tag.short_description = 'Предпросмотр изображения'
    