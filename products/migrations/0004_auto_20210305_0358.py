# Generated by Django 3.1.7 on 2021-03-05 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210305_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='capabilities',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='size',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
