# Generated by Django 4.1.1 on 2022-10-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_housemodel_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='housemodel',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
