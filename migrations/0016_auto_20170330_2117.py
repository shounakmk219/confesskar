# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('confess', '0015_confession_comment_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='GangMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='gang',
            name='member_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='gangmembers',
            name='gang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confess.Gang'),
        ),
        migrations.AddField(
            model_name='gangmembers',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
