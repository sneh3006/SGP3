# Generated by Django 2.2.13 on 2020-10-06 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201006_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionstudent',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birth Date'),
        ),
    ]
