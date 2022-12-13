# Generated by Django 4.1.1 on 2022-11-30 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0063_housemodel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='property_type',
            field=models.CharField(choices=[('residential', 'Residential'), ('commercial', 'Commercial')], default=('commercial', 'Commercial'), max_length=100, null=True),
        ),
    ]