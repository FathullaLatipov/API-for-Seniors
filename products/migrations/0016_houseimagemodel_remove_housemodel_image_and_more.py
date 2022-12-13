# Generated by Django 4.1.1 on 2022-09-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_housemodel_map_housemodel_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='house_images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
        ),
        migrations.RemoveField(
            model_name='housemodel',
            name='image',
        ),
        migrations.AddField(
            model_name='housemodel',
            name='image',
            field=models.ManyToManyField(to='products.houseimagemodel', verbose_name='image'),
        ),
    ]
