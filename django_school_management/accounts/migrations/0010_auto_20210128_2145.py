# Generated by Django 2.2.13 on 2021-01-28 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210128_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='user',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.CommonUserProfile'),
            preserve_default=False,
        ),
    ]
