# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_auto_20171031_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='cliente',
            field=models.ManyToManyField(related_name='cliente_grupos', null=b'true', to='cliente.Cliente', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='precarregamento',
            name='grupo',
            field=models.ManyToManyField(related_name='grupos_pre_carregamento', null=b'true', to='cliente.Grupo', blank=b'true'),
        ),
    ]
