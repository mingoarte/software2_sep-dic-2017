# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-01 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0006_auto_20171101_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Tema:'),
        ),
    ]
