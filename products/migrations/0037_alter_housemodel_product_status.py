# Generated by Django 4.1.1 on 2022-10-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_alter_housemodel_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='product_status',
            field=models.CharField(choices=[('InProgress', 'InProgress'), ('PUBLISH', 'PUBLISH'), ('DELETED', 'DELETED'), ('ARCHIVED', 'ARCHIVED'), ('REJECTED', 'REJECTED')], default=('InProgress', 'InProgress'), max_length=30, null=True),
        ),
    ]
