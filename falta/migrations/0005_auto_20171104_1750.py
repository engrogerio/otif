# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0004_motivoalteraagenda'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MotivoAlteraAgenda',
            new_name='MotivoDeAlteracaoDaAgenda',
        ),
    ]
