# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0012_auto_20170320_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_list',
            field=models.ManyToManyField(to='confess.Confession'),
        ),
    ]
