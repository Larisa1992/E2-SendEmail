# Generated by Django 3.1.2 on 2020-10-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailsend', '0002_auto_20201015_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myemail',
            name='boolsend',
            field=models.BooleanField(default=False, verbose_name='Признак отправки'),
        ),
    ]
