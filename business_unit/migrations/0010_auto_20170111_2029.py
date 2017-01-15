# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0009_auto_20170111_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_businessunit',
            options={'verbose_name': 'Estabs. que o usu\xe1rio pode acessar', 'verbose_name_plural': 'Estabs. que o usu\xe1rio pode acessar'},
        ),
        migrations.AlterModelOptions(
            name='user_estabelecimento',
            options={'verbose_name': 'Estab. do Usu\xe1rio', 'verbose_name_plural': 'Estab. do Usu\xe1rio'},
        ),
    ]
