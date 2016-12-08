# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_renta_pelicula', '0006_auto_20161208_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Estatus'),
        ),
    ]
