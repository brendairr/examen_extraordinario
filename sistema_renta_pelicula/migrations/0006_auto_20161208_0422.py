# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_renta_pelicula', '0005_pelicula_id_pelicula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentapelicula',
            name='hora_renta',
        ),
        migrations.AlterField(
            model_name='rentapelicula',
            name='fecha_renta',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Renta'),
        ),
    ]
