# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-29 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloggs', '0015_auto_20180831_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
                ('count', models.IntegerField(default=0, verbose_name='\u7f51\u7ad9\u8bbf\u95ee\u6b21\u6570')),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u65e5\u8bbf\u95ee\u91cf\u7edf\u8ba1',
                'verbose_name_plural': '\u7f51\u7ad9\u65e5\u8bbf\u95ee\u91cf\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='Userip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='IP\u5730\u5740')),
                ('count', models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u6b21\u6570')),
            ],
            options={
                'verbose_name': '\u8bbf\u95ee\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u8bbf\u95ee\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='VisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='\u7f51\u7ad9\u8bbf\u95ee\u603b\u6b21\u6570')),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u8bbf\u95ee\u603b\u6b21\u6570',
                'verbose_name_plural': '\u7f51\u7ad9\u8bbf\u95ee\u603b\u6b21\u6570',
            },
        ),
    ]
