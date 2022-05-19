# Generated by Django 2.2.10 on 2021-07-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210709_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_details',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='reference',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='ward',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client_details',
            name='pin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
