# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0009_auto_20170314_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='gang',
            name='name',
            field=models.TextField(default='name', max_length=20),
            preserve_default=False,
        ),
    ]
