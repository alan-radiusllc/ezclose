# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-25 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0017_auto_20181223_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ezclose.TeamType'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='ezclose.TeamType'),
        ),
    ]
