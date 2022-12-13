# Generated by Django 3.2.16 on 2022-12-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0072_alter_housemodel_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='product_status',
            field=models.IntegerField(choices=[(0, 'InProgress'), (1, 'PUBLISH'), (2, 'DELETED'), (3, 'ARCHIVED'), (4, 'REJECTED')], default=(0, 'InProgress'), null=True),
        ),
    ]