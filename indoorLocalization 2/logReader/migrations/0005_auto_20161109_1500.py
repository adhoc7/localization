# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logReader', '0004_auto_20161109_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemlogs',
            name='SysLogLatitude',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='systemlogs',
            name='SysLogLongitude',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
