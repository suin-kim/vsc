# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mande', '0004_volunteer_volunteer_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer_detail',
            field=models.CharField(max_length=200),
        ),
    ]