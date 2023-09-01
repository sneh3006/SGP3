# Generated by Django 2.2.13 on 2021-02-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_auto_20210223_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionstudent',
            name='last_exam_name',
        ),
        migrations.RemoveField(
            model_name='admissionstudent',
            name='last_exam_registration',
        ),
        migrations.RemoveField(
            model_name='admissionstudent',
            name='last_exam_result',
        ),
        migrations.RemoveField(
            model_name='admissionstudent',
            name='last_exam_roll',
        ),
        migrations.RemoveField(
            model_name='admissionstudent',
            name='nid_image',
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='children_of_freedom_fighter',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0),
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='exam_name',
            field=models.CharField(choices=[('HSC', 'Higher Secondary Certificate'), ('SSC', 'Secondary School Certificate'), ('DAKHIL', 'Dakhil Exam'), ('VOCATIONAL', 'Vocational')], default='SSC', max_length=10, verbose_name='Exam Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='gpa',
            field=models.DecimalField(decimal_places=2, default=4.5, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='guardian_mobile_number',
            field=models.CharField(default=9018212121, max_length=11, verbose_name='Guardian Mobile Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='passing_year',
            field=models.CharField(default=2020, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='ssc_registration',
            field=models.CharField(default=344342, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionstudent',
            name='tribal_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0),
        ),
        migrations.AlterField(
            model_name='admissionstudent',
            name='admission_policy_agreement',
            field=models.BooleanField(default=False, verbose_name='\n        এই মর্মে অঙ্গীকার করছি যে, ভর্তি হওয়ার সুযোগ পেলে আমি অত্র শিক্ষা প্রতিষ্ঠান ও \n        বাংলাদেশ কারিগরি শিক্ষা বোর্ডের যাবতীয় আইনকানুন মেনে চলব এবং কোন অবস্থাতেই অত্র শিক্ষা প্রতিষ্ঠান, বাংলাদেশ কারিগরি শিক্ষা বোর্ড \n        এবং দেশের আইনের পরিপন্থি কোন কাজে লিপ্ত হব না\n        '),
        ),
    ]
