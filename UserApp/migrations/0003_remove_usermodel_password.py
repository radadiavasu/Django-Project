# Generated by Django 4.1.1 on 2022-09-24 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_usermodel_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='password',
        ),
    ]
