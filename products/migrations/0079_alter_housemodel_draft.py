# Generated by Django 3.2.16 on 2022-12-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0078_alter_housemodel_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='draft',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
