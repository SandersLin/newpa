# Generated by Django 3.0.2 on 2020-01-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20200122_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]