# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_auto_20170927_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='seo_keyword',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='seo keyword'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_keyword',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='seo keyword'),
        ),
    ]
