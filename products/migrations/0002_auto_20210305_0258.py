# Generated by Django 3.1.7 on 2021-03-05 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_es',
        ),
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]
