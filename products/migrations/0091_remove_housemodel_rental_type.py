# Generated by Django 4.0 on 2022-12-23 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0090_housetypemodel_alter_housemodel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housemodel',
            name='rental_type',
        ),
    ]
