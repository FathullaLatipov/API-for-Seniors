# Generated by Django 4.1.1 on 2022-10-21 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_housemodel_archive_housemodel_draft'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housemodel',
            options={'ordering': ['-id'], 'verbose_name': 'House', 'verbose_name_plural': 'Houses'},
        ),
    ]