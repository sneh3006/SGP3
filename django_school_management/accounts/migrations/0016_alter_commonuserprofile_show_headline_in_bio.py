# Generated by Django 4.2.3 on 2023-07-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_commonuserprofile_id_alter_sociallink_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonuserprofile',
            name='show_headline_in_bio',
            field=models.BooleanField(default=False, help_text='I want to use this as my bio.'),
        ),
    ]
