# Generated by Django 4.1.1 on 2022-10-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_amenitiesmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='web_building_type',
            field=models.CharField(max_length=600, null=True, verbose_name='web_building_type'),
        ),
        migrations.AddField(
            model_name='housemodel',
            name='web_object',
            field=models.CharField(max_length=300, null=True, verbose_name='web_object'),
        ),
        migrations.AddField(
            model_name='housemodel',
            name='web_rental_type',
            field=models.CharField(max_length=500, null=True, verbose_name='web_rental_type'),
        ),
        migrations.AddField(
            model_name='housemodel',
            name='web_type',
            field=models.CharField(max_length=400, null=True, verbose_name='web_type'),
        ),
    ]
