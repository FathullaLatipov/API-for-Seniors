# Generated by Django 4.1.1 on 2022-11-05 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0050_alter_amenitiesmodel_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricelistmodel',
            name='product',
        ),
        migrations.AddField(
            model_name='housemodel',
            name='price_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='price_type', to='products.pricelistmodel'),
            preserve_default=False,
        ),
    ]