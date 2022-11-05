# Generated by Django 3.2.9 on 2022-11-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_messageentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageentity',
            name='length',
            field=models.SmallIntegerField(null=True, verbose_name='Длинна'),
        ),
        migrations.AlterField(
            model_name='messageentity',
            name='offset',
            field=models.SmallIntegerField(null=True, verbose_name='Офсет'),
        ),
        migrations.AlterField(
            model_name='messageentity',
            name='type',
            field=models.CharField(blank=True, choices=[('url', 'URL'), ('text_url', 'Text URL'), ('bold', 'Bold'), ('italic', 'Italic'), ('underline', 'Underline'), ('email', 'Email'), ('phone', 'Phone'), ('mention_name', 'Mention Name'), ('mention', 'Mention')], max_length=20),
        ),
    ]