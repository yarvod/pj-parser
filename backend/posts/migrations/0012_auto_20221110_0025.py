# Generated by Django 3.2.9 on 2022-11-09 21:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_rawpost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageentity',
            name='type',
            field=models.CharField(blank=True, choices=[('url', 'URL'), ('text_url', 'Text URL'), ('bold', 'Bold'), ('italic', 'Italic'), ('underline', 'Underline'), ('email', 'Email'), ('phone', 'Phone'), ('mention_name', 'Mention Name'), ('mention', 'Mention'), ('hashtag', 'Hashtag')], max_length=20, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='rawpost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 21, 25, 47, 758498, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]
