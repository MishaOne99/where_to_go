from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, verbose_name='Полное описание')
    lon = models.FloatField(null=True, verbose_name='Долгота')
    lat = models.FloatField(null=True, verbose_name='Широта')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Images(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    number = models.IntegerField(blank=True, verbose_name='Номер изображения')
    image = models.ImageField(blank=True)
    
    def __str__(self) -> str:
        return f'№{self.number} - {self.title}'
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'