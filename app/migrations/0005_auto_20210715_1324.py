# Generated by Django 2.2.10 on 2021-07-15 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210715_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_details',
            old_name='state',
            new_name='block',
        ),
    ]
