# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-18 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=128)),
                ('answer', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='generic',
            name='preguntas',
            field=models.ManyToManyField(related_name='encuesta', to='builder.Pregunta'),
        ),
    ]
