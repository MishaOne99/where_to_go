from django.db import models
from django.utils.safestring import mark_safe


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, null=True, verbose_name='Полное описание')
    lat = models.FloatField(blank=True, null=True, verbose_name='Широта')
    lon = models.FloatField(blank=True, null=True, verbose_name='Долгота')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Название локации', related_name='images')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    image_id = models.PositiveIntegerField(db_index=True, default=0, verbose_name='Номер изображения')
    
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 200px; height: 200px;" />')
        return "No Image"

    image_tag.short_description = 'Image Preview'
    
    def __str__(self) -> str:
        return str(self.place)
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        
        ordering = ['image_id']