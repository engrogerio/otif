# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta', '0006_auto_20171109_1853'),
        ('pedido', '0010_auto_20171104_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motivosatrasocarregamento',
            name='business_unit',
        ),
        migrations.RemoveField(
            model_name='motivosatrasocarregamento',
            name='carregamento',
        ),
        migrations.RemoveField(
            model_name='motivosatrasocarregamento',
            name='motivo',
        ),
        migrations.AddField(
            model_name='carregamento',
            name='ds_obs_atraso',
            field=models.CharField(max_length=300, null=b'true', verbose_name=b'Observa\xc3\xa7\xc3\xa3o Atraso', blank=b'true'),
        ),
        migrations.AddField(
            model_name='carregamento',
            name='motivo_atraso',
            field=models.ForeignKey(related_name='motivo_atraso', verbose_name=b'Motivo do Atraso', blank=b'true', to='falta.MotivoAtraso', null=b'true'),
        ),
        migrations.DeleteModel(
            name='MotivosAtrasoCarregamento',
        ),
    ]
