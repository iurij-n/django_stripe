# Generated by Django 3.2.16 on 2022-11-21 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]
