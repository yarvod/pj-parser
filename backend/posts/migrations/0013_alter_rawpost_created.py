# Generated by Django 3.2.9 on 2022-11-09 21:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20221110_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 21, 35, 41, 972674, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]
