# Generated by Django 3.2.9 on 2022-12-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_news_raw_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
