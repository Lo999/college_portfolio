# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-06 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0016_auto_20180806_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=250)),
                ('likes', models.PositiveSmallIntegerField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.Entry')),
            ],
        ),
    ]
