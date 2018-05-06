# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from port.models import Port
from port.views import name1, parser, find

urlpatterns = [url(r'^$', ListView.as_view(queryset=Port.objects.all(),template_name="port/portmain.html")),
               url(r'^search/',find,name='find'),
               url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Port, template_name='port/port.html')),
				               
               url(r'^parser',parser,name='parser'),
               url(r'^(?P<port_name>.*)$', name1,name='name1'),
               ]

#url(r'^(?P<port_name>.*)$', name1,name='name1'),