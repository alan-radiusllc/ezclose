# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0010_auto_20181104_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='brokerage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezclose.Brokerage'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isRealtor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='defaultName', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone1',
            field=models.CharField(default=-4182, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone1Type',
            field=models.CharField(blank=True, choices=[('CELL', 'cell'), ('OFFICE', 'office'), ('HOME', 'home'), ('ADMIN', 'admin')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone2Type',
            field=models.CharField(blank=True, choices=[('CELL', 'cell'), ('OFFICE', 'office'), ('HOME', 'home'), ('ADMIN', 'admin')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
