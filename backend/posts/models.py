from ckeditor.fields import RichTextField
from django.db import models


class RawPost(models.Model):
    channel = models.ForeignKey('bot.Channel', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст публикации', blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


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
