# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-24 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggs', '0010_newpaper_newpaper_classify'),
    ]

    operations = [
        migrations.CreateModel(
            name='art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arts', models.TextField(null=True)),
            ],
        ),
    ]
