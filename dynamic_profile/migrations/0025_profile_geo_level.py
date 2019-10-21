# Generated by Django 2.2.6 on 2019-10-21 06:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_profile', '0024_auto_20191021_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='geo_level',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=['country', 'province', 'district', 'municipality', 'ward', 'subplace', 'smallarea'], size=None),
        ),
    ]