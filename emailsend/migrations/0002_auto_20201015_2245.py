# Generated by Django 3.1.2 on 2020-10-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailsend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myemail',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]