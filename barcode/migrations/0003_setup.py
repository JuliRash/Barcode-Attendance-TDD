# Generated by Django 3.1 on 2021-03-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0002_auto_20210320_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=2000)),
                ('organization_description', models.TextField(blank=True)),
                ('organization_location', models.CharField(max_length=255)),
                ('organization_logo', models.ImageField(blank=True, upload_to='setup')),
            ],
            options={
                'verbose_name_plural': 'setup',
            },
        ),
    ]
