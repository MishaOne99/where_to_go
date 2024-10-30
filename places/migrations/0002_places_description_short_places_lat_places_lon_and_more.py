# Generated by Django 4.2.16 on 2024-10-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='places',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='places',
            name='lon',
            field=models.FloatField(null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='places',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
