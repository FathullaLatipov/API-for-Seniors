# Generated by Django 4.1.1 on 2022-10-21 21:41

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', user.models.MyUserManager()),
            ],
        ),
    ]
