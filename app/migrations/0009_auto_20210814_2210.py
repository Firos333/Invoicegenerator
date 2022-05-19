# Generated by Django 2.2.10 on 2021-08-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210716_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_details',
            old_name='address',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='client_details',
            old_name='reference',
            new_name='education',
        ),
        migrations.RenameField(
            model_name='client_details',
            old_name='ward',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='block',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='id_file',
        ),
        migrations.RemoveField(
            model_name='client_details',
            name='img',
        ),
        migrations.AddField(
            model_name='client_details',
            name='address_line2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client_details',
            name='is_banking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client_details',
            name='is_exp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client_details',
            name='is_smartphone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client_details',
            name='taluk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client_details',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
