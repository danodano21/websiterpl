# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-16 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20200516_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]