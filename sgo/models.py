# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class OtifModel(models.Model):
    # All otf specific models should extend this class instead of models.Model directly.
    dt_atlz = models.DateTimeField('Data atualização')
    usr_atlz = models.ForeignKey(User , null='true', blank='true', )

    class Meta:
        abstract = True
