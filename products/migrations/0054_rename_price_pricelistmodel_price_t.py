# Generated by Django 4.1.1 on 2022-11-10 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0053_alter_housemodel_amenities_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricelistmodel',
            old_name='price',
            new_name='price_t',
        ),
    ]
