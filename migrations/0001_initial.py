# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Confession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField(max_length=20)),
                ('entry', models.TextField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='confession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confess.Confession'),
        ),
    ]