# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-19 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Tema:')),
                ('fecha_publ', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='fecha de creacion:')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='fecha de creacion:')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreguntaFaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=100, verbose_name='Pregunta:')),
                ('respuesta', models.TextField(max_length=250, verbose_name='Respuesta:')),
                ('faq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faqs.Faq')),
                ('tema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faqs.Categoria')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='faq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faqs.Faq'),
        ),
    ]
