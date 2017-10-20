# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_opcion', models.CharField(max_length=200, verbose_name='Opción:')),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pregunta', models.CharField(max_length=200, verbose_name='Pregunta:')),
                ('fecha_publ', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='fecha de publicación')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='builder.Template')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.Pregunta'),
        ),
    ]
