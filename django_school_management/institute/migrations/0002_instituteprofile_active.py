# Generated by Django 2.2.13 on 2021-01-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituteprofile',
            name='active',
            field=models.BooleanField(default=False, unique=True),
        ),
    ]
