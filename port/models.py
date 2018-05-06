# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Port(models.Model):
    portid = models.IntegerField(primary_key=True)
    portname = models.TextField(default='')
    description = models.TextField(default='')
    variant = models.TextField(default='')
    portdir = models.TextField(default='')
    platform = models.TextField(default='')
    cur_version = models.TextField(default='')
    license = models.TextField(default='')
    long_desc = models.TextField(default='')
    homepage = models.TextField(default='')

    def __str__(self):
        return self.portname
