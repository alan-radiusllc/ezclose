# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]