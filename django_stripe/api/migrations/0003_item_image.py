# Generated by Django 3.2.16 on 2022-11-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20221120_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, height_field=270, upload_to='images', verbose_name='Изображение товара', width_field=270),
        ),
    ]
