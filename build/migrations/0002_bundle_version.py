# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-29 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='version',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='build.Version'),
        ),
    ]
