# Generated by Django 4.1.1 on 2022-10-04 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_mastermodel_address_alter_mapmodel_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mastermodel',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='mastermodel',
            name='address',
        ),
        migrations.DeleteModel(
            name='MasterActivity',
        ),
        migrations.DeleteModel(
            name='MasterModel',
        ),
    ]