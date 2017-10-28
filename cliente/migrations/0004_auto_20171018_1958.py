# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20170803_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='hr_lim_carga',
            field=models.TimeField(null=b'true', verbose_name=b'Limite de atraso na chegada do caminh\xc3\xa3o (hs)', blank=b'true'),
        ),
    ]
