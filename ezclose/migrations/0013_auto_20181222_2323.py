# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-22 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0012_remove_team_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('REALTOR', 'Realtor'), ('REAL_ESTATE_BROKER', 'Real Estate Broker'), ('LENDER', 'Lender'), ('MORTGAGE_BROKER', 'Mortgage Broker'), ('BANKER', 'Banker'), ('CLOSING', 'Closing'), ('ATTORNEY', 'Attorney'), ('INSURANCE', 'Home Owners Insurance'), ('INSPECTOR', 'Home Inspector'), ('SPECIALTY_INSPECTOR', 'Speialty Inspector'), ('HOME_REPAIR', 'Home Repair'), ('CONTRACTOR', 'Contractor'), ('WARRANTY', 'Home Warranty'), ('OTHER', 'Other')], max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='teammember',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TeamMembers', to='ezclose.TeamType'),
        ),
    ]
