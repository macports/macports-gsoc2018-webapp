# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from port.models import Port
import json
# Create your views here.
def name1(request,port_name):
	data= Port.objects.filter(portname=port_name).last()
	return render(request,'port/port.html',{"port":data})


def parser(request):
	data1=json.loads(open('port/testing2.json').read())
	count=0

	try:
		id=Port.objects.latest("portid").portid
		id = id + 1
	except Port.DoesNotExist:
		id=0

	for b in data1:
		
		p1n=b['name']
		if 'description' in b:
			d1e=b['description']
		else:
			d1e=''

		if 'variants' in b:
			v1a=b['variants']
		else:
			v1a=''

		if 'portdir' in b:
			p1d=b['portdir']
		else:
			p1d=''
			
		c = Port.objects.create(portid=id, portname=p1n, description=d1e, variant=v1a, portdir=p1d)
		count +=1
		id +=1
		#print("completed the INSERT")
		#print(c.fetchall())

	'''
	b = jsonparser(k)
	p1n = b['name']
	d1e = b['description']
	v1a = b['variants']
	p1d = b['portdir']
	c = Port.objects.create(portname=p1n, description=d1e, variant=v1a, portdir=p1d)
	'''
	#from django.db import connection
	#to print the query in console
	#data= Port.objects.filter(portname=p1n)
	#print connection.queries[-1]
	
	#return render(request,'port/data.html',{"port1":data.last()})
	return render(request,'port/data.html',{"port1":count})




def find(request):
	if request.method == 'POST':
			port_name = request.POST.get('textfield', None)
			data=Port.objects.filter(portname__startswith=port_name)
			
			return render(request, 'port/portmain.html',{"object_list":data,"flag":1})
	else:
		return render(request,'port/portmain.html')
	
