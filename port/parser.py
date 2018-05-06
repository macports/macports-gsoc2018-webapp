# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django
import os

from django.conf import settings
#settings.configure()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../mysite.settings')
from django.db import models


from models import Port



k = """{
    "variants"         : "temp",
    "portdir"          : "lang/game",
    "description"      : "An interpreted coding language",
    "homepage"         : "https://www.python.org/",
    "depends_run"      : "port:python_select",
    "epoch"            : "0",
    "platforms"        : "darwin",
    "name"             : "game",
    "depends_lib"      : "port:gettext path:lib/libssl.dylib:openssl",
    "license"          : "PSF",
    "long_description" : "Python is an interpreted, interactive, object-oriented programming language.",
    "maintainers"      : "fourdigits.nl:roel openmaintainer",
    "categories"       : "lang",
    "version"          : "2.4.6",
    "revision"         : "12"
}
"""


def jsonparser(json1):
    obj = json.loads(json1)
    return obj


b = jsonparser(k)
p1n = b['name']
d1e = b['description']
v1a = b['variants']
p1d = b['portdir']

settings.configure()

c = Port.objects.create(portname=p1n, description=d1e, variant=v1a, portdir=p1d)
