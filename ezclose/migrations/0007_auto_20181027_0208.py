# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0006_auto_20181027_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='tag1',
            field=models.CharField(blank=True, choices=[('RADON', 'Radon'), ('TITLE_5', 'Title V'), ('SHORT', 'SHORT'), ('SPECIAL_INSP', 'Special Inspection'), ('OTHER', 'Other')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='tag2',
            field=models.CharField(blank=True, choices=[('RADON', 'Radon'), ('TITLE_5', 'Title V'), ('SHORT', 'SHORT'), ('SPECIAL_INSP', 'Special Inspection'), ('OTHER', 'Other')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='tag3',
            field=models.CharField(blank=True, choices=[('RADON', 'Radon'), ('TITLE_5', 'Title V'), ('SHORT', 'SHORT'), ('SPECIAL_INSP', 'Special Inspection'), ('OTHER', 'Other')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='tag1',
            field=models.CharField(blank=True, choices=[('RADON', 'Radon'), ('TITLE_5', 'Title V'), ('SHORT', 'SHORT'), ('SPECIAL_INSP', 'Special Inspection'), ('OTHER', 'Other')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='tag2',
            field=models.CharField(blank=True, choices=[('RADON', 'Radon'), ('TITLE_5', 'Title V'), ('SHORT', 'SHORT'), ('SPECIAL_INSP', 'Special Inspection'), ('OTHER', 'Other')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='tag3',
            field=models.CharField(blank=True, choices=[('RADON', 'Radon'), ('TITLE_5', 'Title V'), ('SHORT', 'SHORT'), ('SPECIAL_INSP', 'Special Inspection'), ('OTHER', 'Other')], max_length=12, null=True),
        ),
    ]