# Generated by Django 3.0.6 on 2020-05-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('mobnum', models.IntegerField()),
                ('parentmobnum', models.IntegerField()),
                ('course', models.TextField()),
            ],
        ),
    ]
