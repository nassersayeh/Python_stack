# Generated by Django 2.2.4 on 2021-05-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
