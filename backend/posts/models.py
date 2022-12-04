import logging

import requests
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.timezone import now
from rest_framework import serializers

from posts.constants import MessageEntityTypes


logger = logging.getLogger(__name__)


class RawPost(models.Model):
    channel = models.ForeignKey('bot.Channel', on_delete=models.CASCADE, verbose_name='Канал')
    text = models.TextField(verbose_name='Текст публикации', blank=True)
    created = models.DateTimeField(default=now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return truncatechars(self.text, 35)


class MessageEntity(models.Model):
    post = models.ForeignKey(to='RawPost', verbose_name='Пост', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст', blank=True)
    type = models.CharField(choices=MessageEntityTypes.CHOICES, max_length=20, blank=True, verbose_name='Тип')
    offset = models.SmallIntegerField(verbose_name='Офсет', null=True)
    length = models.SmallIntegerField(verbose_name='Длинна', null=True)
    url = models.URLField(verbose_name='Ссылка', blank=True, null=True)

    class Meta:
        verbose_name = 'Message Entity'
        verbose_name_plural = 'Message Entities'


class Vacancy(models.Model):
    by_admin = models.BooleanField(default=True, verbose_name='Создана админом')
    company_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название компании/организации')
    contact_telegram = models.CharField(max_length=50, null=True, blank=True, verbose_name='Телеграм для контакта')
    contact_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Телефон для контакта')
    contact_email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Почта для контакта')
    contact_site = models.CharField(max_length=255, null=True, blank=True, verbose_name='Сайт компании для контакта')
    company_description = RichTextField(null=True, blank=True, verbose_name='Описание компании')

    title = models.CharField(max_length=255, verbose_name='Название')
    about = RichTextField(null=True, blank=True, verbose_name='Описание вакансии')
    duties = RichTextField(null=True, blank=True, verbose_name='Обязанности сотрудника')
    requirements = RichTextField(null=True, blank=True, verbose_name='Требования к сотруднику')
    skills = RichTextField(null=True, blank=True, verbose_name='Навыки сотрудника')
    conditions = RichTextField(null=True, blank=True, verbose_name='Условия работы')

    by_agreement = models.BooleanField(default=False, verbose_name='Зарплата по договоренности?')
    salary_from = models.PositiveIntegerField(null=True, blank=True, verbose_name='Зарплата мин')
    salary_to = models.PositiveIntegerField(null=True, blank=True, verbose_name='Зарплата макс')

    distant_work = models.BooleanField(default=False, verbose_name='Возможность дистанционной работы')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')

    experience_from = models.PositiveSmallIntegerField(verbose_name='Опыт работы от, лет', default=0)
    experience_to = models.PositiveSmallIntegerField(verbose_name='Опыт работы до, лет', default=0)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class News(models.Model):
    is_active = models.BooleanField(verbose_name='Активно', default=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=False)
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField('Дата создания', default=now)
    publish_date = models.DateTimeField('Дата публикации', blank=True, null=True)
    raw_post = models.ForeignKey(to='RawPost', verbose_name='Сырой пост', on_delete=models.SET_NULL, null=True,
                                 blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return truncatechars(self.text, 35)

    def publish(self):
        data = NewsSerializer(self).data
        resp = requests.post(
            url=settings.NEWS_URL,
            auth=(settings.PHYSTECHJOB_USER, settings.PHYSTECHJOB_PWD),
            json=data
        )
        logger.info(resp.status_code)
        if resp.status_code == '201':
            self.is_published = True
            self.publish_date = now()
            self.save()


class NewsSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('text', 'date', 'is_active')

    def get_text(self, obj):
        text = obj.text
        text.replace('\n', '<br/>')
        return text
