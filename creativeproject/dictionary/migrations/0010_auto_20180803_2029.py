# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0009_auto_20180731_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='english_definition',
            new_name='definition',
        ),
    ]