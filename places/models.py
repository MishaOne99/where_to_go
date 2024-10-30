from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    lon = models.FloatField(null=True, verbose_name='Долгота')
    lat = models.FloatField(null=True, verbose_name='Широта')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'