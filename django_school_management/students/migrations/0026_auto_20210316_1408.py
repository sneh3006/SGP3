# Generated by Django 2.2.13 on 2021-03-16 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0025_auto_20210223_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counselingcomment',
            name='counselor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
