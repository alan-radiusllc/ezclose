# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-23 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0015_auto_20181223_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamtype',
            old_name='type',
            new_name='ttype',
        ),
    ]