# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170621_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
