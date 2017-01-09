# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_unit', '0001_initial'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='business_unit',
            field=models.ForeignKey(to='business_unit.BusinessUnit', default='n\xe3o selecionado', to_field=b'unit'),
            preserve_default=False,
        ),
    ]
