# Generated by Django 3.2.9 on 2022-11-09 21:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_messageentity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawpost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 21, 24, 49, 216186, tzinfo=utc)),
        ),
    ]
