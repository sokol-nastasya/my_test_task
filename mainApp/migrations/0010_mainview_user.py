# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-02 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0009_auto_20181002_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainview',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
