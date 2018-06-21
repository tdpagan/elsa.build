# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-11 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0005_remove_bundle_directory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternate_id', models.CharField(max_length=100)),
                ('alternate_title', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
    ]