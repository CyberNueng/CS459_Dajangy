# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-26 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20180309_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterField(
            model_name='rent',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='stop',
            field=models.DateTimeField(blank=True),
        ),
    ]