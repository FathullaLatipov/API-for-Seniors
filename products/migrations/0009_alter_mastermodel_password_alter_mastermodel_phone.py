# Generated by Django 4.1.1 on 2022-09-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_mastermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastermodel',
            name='password',
            field=models.CharField(max_length=100, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='mastermodel',
            name='phone',
            field=models.PositiveIntegerField(verbose_name='phone'),
        ),
    ]
