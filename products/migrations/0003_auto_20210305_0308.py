# Generated by Django 3.1.7 on 2021-03-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210305_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='categories/pictures/'),
        ),
    ]
