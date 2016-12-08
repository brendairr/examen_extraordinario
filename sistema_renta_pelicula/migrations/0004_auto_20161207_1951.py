# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_renta_pelicula', '0003_auto_20161207_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='actores',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='actor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sistema_renta_pelicula.Actores'),
        ),
    ]
