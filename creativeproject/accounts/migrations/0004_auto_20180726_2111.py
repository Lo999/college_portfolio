# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_language'),
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='languages',
            new_name='other_languages',
        ),
        migrations.AddField(
            model_name='profile',
            name='native_languages',
            field=models.ManyToManyField(blank=True, related_name='native_languages', to='dictionary.Language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='target_languages',
            field=models.ManyToManyField(blank=True, related_name='target_languages', to='dictionary.Language'),
        ),
    ]
