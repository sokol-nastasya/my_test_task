# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-02 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_auto_20180427_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainview',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
