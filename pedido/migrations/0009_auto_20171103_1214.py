# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_auto_20171029_0943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carregamento',
            options={'permissions': (('can_schedule', 'Pode Agendar Pedidos'), ('can_load', 'Pode Carregar'))},
        ),
    ]
