# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0007_motivosatrasocarregamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivosatrasocarregamento',
            name='carregamento',
            field=models.ForeignKey(related_name='carregamento_motivo', verbose_name=b'Carregamento', blank=b'true', to='pedido.Carregamento', null=b'true'),
        ),
        migrations.AlterField(
            model_name='motivosatrasocarregamento',
            name='ds_obs',
            field=models.CharField(max_length=300, null=b'true', verbose_name=b'Observa\xc3\xa7\xc3\xa3o', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='motivosatrasocarregamento',
            name='motivo',
            field=models.ForeignKey(related_name='motivo_atraso', verbose_name=b'Motivo do Atraso', blank=b'true', to='falta.Motivo', null=b'true'),
        ),
    ]
