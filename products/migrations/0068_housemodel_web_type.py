# Generated by Django 4.1.1 on 2022-11-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0067_alter_housemodel_pm_general_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='web_type',
            field=models.CharField(max_length=400, null=True, verbose_name='web_type'),
        ),
    ]
