# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-02 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0011_auto_20181123_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='client',
        ),
    ]
