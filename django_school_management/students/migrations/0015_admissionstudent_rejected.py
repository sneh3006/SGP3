# Generated by Django 2.2.13 on 2020-12-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_admissionstudent_migration_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionstudent',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
