# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_renta_pelicula', '0004_auto_20161207_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='id_pelicula',
            field=models.CharField(default=0, max_length=4, verbose_name='ID Pelicula'),
            preserve_default=False,
        ),
    ]
