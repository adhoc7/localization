# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logParser', '0002_auto_20161110_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logparser',
            name='LogFileName',
            field=models.FileField(upload_to='./logParser/LogFiles/'),
        ),
    ]
