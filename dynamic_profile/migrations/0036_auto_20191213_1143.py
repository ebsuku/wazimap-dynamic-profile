# Generated by Django 2.2.6 on 2019-12-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_profile', '0035_auto_20191206_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatorprofile',
            name='chart_design',
            field=models.CharField(default='--half-width', max_length=25),
        ),
    ]