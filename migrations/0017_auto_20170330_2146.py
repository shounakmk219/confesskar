# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confess', '0016_auto_20170330_2117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GangMembers',
            new_name='GangMember',
        ),
    ]