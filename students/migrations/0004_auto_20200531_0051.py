# Generated by Django 3.0.6 on 2020-05-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200530_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissions',
            name='firstname',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='admissions',
            name='surname',
            field=models.TextField(),
        ),
    ]