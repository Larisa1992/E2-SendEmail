# Generated by Django 3.1.2 on 2020-10-20 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emailsend', '0003_auto_20201016_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myemail',
            name='createdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]