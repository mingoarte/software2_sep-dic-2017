# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-02 04:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('builder', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(null=True)),
                ('form_json', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='builder.Template')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
