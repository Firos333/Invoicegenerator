# Generated by Django 2.2.10 on 2021-08-15 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210814_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_details',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='longitude',
        ),
    ]