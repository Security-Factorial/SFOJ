# Generated by Django 3.1.3 on 2021-08-24 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfoj_system', '0002_auto_20210824_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='Hit',
        ),
        migrations.RemoveField(
            model_name='board',
            name='Success_per',
        ),
        migrations.RemoveField(
            model_name='board',
            name='UserID',
        ),
    ]