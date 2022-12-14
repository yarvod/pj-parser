# Generated by Django 3.2.9 on 2022-11-05 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221105_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('type', models.CharField(choices=[('url', 'URL'), ('text_url', 'Text URL'), ('bold', 'Bold'), ('italic', 'Italic'), ('underline', 'Underline'), ('email', 'Email'), ('phone', 'Phone'), ('mention_name', 'Mention Name'), ('mention', 'Mention')], default='bold', max_length=20)),
                ('offset', models.SmallIntegerField(verbose_name='Офсет')),
                ('length', models.SmallIntegerField(verbose_name='Длинна')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.rawpost', verbose_name='Пост')),
            ],
        ),
    ]
