# Generated by Django 4.0 on 2022-12-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0080_categorymodel_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='how_sale',
            field=models.CharField(max_length=200, null=True, verbose_name='Как продавать'),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='pr_amenities', to='products.AmenitiesModel', verbose_name='amenities'),
        ),
    ]