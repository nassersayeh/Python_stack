# Generated by Django 2.2.4 on 2021-05-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20210524_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='authours',
            name='note',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
