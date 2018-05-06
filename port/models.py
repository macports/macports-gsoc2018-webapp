# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Port(models.Model):
    portid = models.IntegerField(primary_key=True)
    portname = models.TextField()
    description = models.TextField()
    variant = models.TextField()
    portdir = models.TextField()

    def __str__(self):
        return self.portname
