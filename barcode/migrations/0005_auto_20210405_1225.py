# Generated by Django 3.1 on 2021-04-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0004_auto_20210405_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]