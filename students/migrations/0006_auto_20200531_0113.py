# Generated by Django 3.0.6 on 2020-05-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20200531_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissions',
            name='mobnum',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='admissions',
            name='parentmobnum',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
