# Generated by Django 2.2.10 on 2021-07-08 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_details',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
