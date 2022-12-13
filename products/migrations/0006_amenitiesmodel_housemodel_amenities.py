# Generated by Django 4.1.1 on 2022-09-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_housemodel_building_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmenitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'All_amenities',
                'verbose_name_plural': 'All_amenities',
            },
        ),
        migrations.AddField(
            model_name='housemodel',
            name='amenities',
            field=models.ManyToManyField(to='products.amenitiesmodel', verbose_name='amenities'),
        ),
    ]