# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_grupo_precarregamento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'verbose_name_plural': 'Grupos de Cliente'},
        ),
    ]
