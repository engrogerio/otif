# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_auto_20161119_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='hr_grade',
            field=models.IntegerField(blank=b'true', null=b'true', verbose_name=b'Hor\xc3\xa1rio', choices=[(0, b'0:00'), (1, b'1:00'), (2, b'2:00'), (3, b'3:00'), (4, b'4:00'), (5, b'5:00'), (6, b'6:00'), (7, b'7:00'), (8, b'8:00'), (9, b'9:00'), (10, b'10:00'), (11, b'11:00'), (12, b'12:00'), (13, b'13:00'), (14, b'14:00'), (15, b'15:00'), (16, b'16:00'), (17, b'17:00'), (18, b'18:00'), (19, b'19:00'), (20, b'20:00'), (21, b'21:00'), (22, b'22:00'), (23, b'23:00')]),
        ),
    ]
