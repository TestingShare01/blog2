# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-22 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggs', '0009_newpaper_newpaper_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpaper',
            name='Newpaper_classify',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]