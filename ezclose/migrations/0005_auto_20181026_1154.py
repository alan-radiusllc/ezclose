# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 11:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezclose', '0004_transactions_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brokerage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('street', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=128, null=True)),
                ('phone1', models.CharField(blank=True, max_length=20, null=True)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('manager', models.CharField(blank=True, max_length=128, null=True)),
                ('mngrphone', models.CharField(blank=True, max_length=20, null=True)),
                ('mngremail', models.EmailField(blank=True, max_length=254, null=True)),
                ('locality', models.CharField(blank=True, default='', max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mls', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('street', models.CharField(blank=True, max_length=128, null=True)),
                ('street2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='street',
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='client',
            name='street2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone1Type',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone2Type',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='street',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='defaultmilestones',
            name='type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='brokerage',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='category',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='group',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='locality',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='milestone',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='milestoneDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='tag1',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='tag2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='tag3',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='defaulttasks',
            name='wbs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='brokerage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezclose.Brokerage'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone1Type',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone2Type',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='category',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='dueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='group',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='milestone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezclose.Milestone'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='ripeDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='wbs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='lastActivity',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezclose.Property'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
