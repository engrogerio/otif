# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carregamento',
            old_name='ds_get_status_lib',
            new_name='ds_status_lib',
        ),
        migrations.RemoveField(
            model_name='carregamento',
            name='st_chegada',
        ),
        migrations.RemoveField(
            model_name='carregamento',
            name='st_libera',
        ),
    ]
