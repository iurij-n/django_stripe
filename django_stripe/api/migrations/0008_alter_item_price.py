# Generated by Django 3.2.16 on 2022-11-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(help_text='Цена товара в копейках', verbose_name='Цена'),
        ),
    ]
