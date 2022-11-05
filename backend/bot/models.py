from django.db import models


class Channel(models.Model):
    is_active = models.BooleanField(default=False)
    username = models.CharField(unique=True, verbose_name='Юзернейм', max_length=50)
    name = models.CharField(verbose_name='Название канала', max_length=100)
    link = models.URLField(verbose_name='Ссылка на канал', max_length=100, null=True, blank=True)
    sender_id = models.CharField(unique=True, verbose_name='Телеграм отправитель id', max_length=50, blank=True,
                                 null=True)
    uid = models.CharField(unique=True, verbose_name='Телеграм id', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

    def __str__(self):
        return self.name
