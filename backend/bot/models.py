from django.contrib.postgres.fields import ArrayField
from django.db import models


class Channel(models.Model):
    is_active = models.BooleanField(default=False)
    username = models.CharField(unique=True, verbose_name='Юзернейм', max_length=50)
    name = models.CharField(verbose_name='Название канала', max_length=100)
    link = models.URLField(verbose_name='Ссылка на канал', max_length=100, null=True, blank=True)
    filter_by_hashtag = models.BooleanField(verbose_name='Фильтровать по хэштегу', default=False)
    hashtags = ArrayField(models.CharField(max_length=20), verbose_name='Хэштеги', blank=True, null=True,
                          help_text='str через запятую')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

    def __str__(self):
        return self.name
