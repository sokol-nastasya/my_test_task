# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20180424_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainview',
            name='keywords',
            field=models.ManyToManyField(related_name='keywords', related_query_name='keyword', to='mainApp.Keywords'),
        ),
    ]
