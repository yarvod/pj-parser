# Generated by Django 3.2.9 on 2022-11-04 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
        ('posts', '0003_auto_20221104_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpost',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.channel'),
        ),
        migrations.DeleteModel(
            name='Channel',
        ),
    ]