# Generated by Django 3.2.4 on 2021-06-20 03:36

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20210620_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
    ]
