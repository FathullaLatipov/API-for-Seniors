# Generated by Django 4.1.1 on 2022-09-22 15:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_mastermodel_password_alter_mastermodel_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mastermodel',
            name='my_field2',
        ),
        migrations.AddField(
            model_name='mastermodel',
            name='activity',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('plumber', 'plumber'), ('electric', 'electric'), ('furniture maker', 'furniture maker'), ('window master', 'window master'), ('Cleaner', 'Cleaner')], max_length=30, null=True),
        ),
    ]