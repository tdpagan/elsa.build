# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-14 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0007_citation_information'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citation_information',
            options={},
        ),
        migrations.AddField(
            model_name='product_document',
            name='acknowledgement_text',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='author_list',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='copyright',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='document_editions',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='document_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='doi',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='editor_list',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='publication_date',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_document',
            name='revision_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
