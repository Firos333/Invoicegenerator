# Generated by Django 2.2.10 on 2021-08-17 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210817_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_details',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]