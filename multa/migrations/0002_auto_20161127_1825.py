# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multa', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carregamento',
            new_name='MultaCarregamento',
        ),
        migrations.RenameModel(
            old_name='Item',
            new_name='MultaItem',
        ),
    ]
