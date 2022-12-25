# Generated by Django 4.0 on 2022-12-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0100_alter_housemodel_object_alter_housemodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='building_type',
            field=models.CharField(blank=True, choices=[('кирпич', 'кирпич'), ('монолит', 'монолит'), ('панель', 'панель'), ('блочный', 'блочный')], default=None, max_length=50, null=True, verbose_name='building_type'),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='property_type',
            field=models.CharField(choices=[('жилая', 'жилая'), ('коммерческая', 'коммерческая')], default=('коммерческая', 'коммерческая'), max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='rental_type',
            field=models.CharField(blank=True, choices=[('длительно', 'Длительно'), ('несколько месяцев', 'несколько месяцев'), ('посуточно', 'посуточно')], default=('несколько месяцев', 'несколько месяцев'), max_length=200, null=True),
        ),
    ]