# Generated by Django 2.2.4 on 2021-05-25 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_show_updatedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='updatedate',
        ),
    ]
