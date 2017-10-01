# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_auto_20170227_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seo_keyword',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=django_prices.models.PriceField(currency='VND', decimal_places=2, max_digits=12, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='price_override',
            field=django_prices.models.PriceField(blank=True, currency='VND', decimal_places=2, max_digits=12, null=True, verbose_name='price override'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cost_price',
            field=django_prices.models.PriceField(blank=True, currency='VND', decimal_places=2, max_digits=12, null=True, verbose_name='cost price'),
        ),
    ]