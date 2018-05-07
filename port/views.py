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
		id=1

	for b in data1:
		
		port_name=b['name']
		if 'description' in b:
			desc=b['description']
		else:
			desc=''

		if 'variants' in b:
			variant=b['variants']
		else:
			variant=''

		if 'portdir' in b:
			port_dir=b['portdir']
		else:
			port_dir=''

		if 'platforms' in b:
			platform=b['platforms']
		else:
			platform=''
		
		if 'version' in b:
			version=b['version']
		else:
			version=''
		
		if 'homepage' in b:
			homepage=b['homepage']
		else:
			homepage=''
		
		if 'license' in b:
			license=b['license']
		else:
			license=''
			
		if 'long_description' in b:
			long_description=b['long_description']
		else:
			long_description=''
		
		c = Port.objects.create(portid=id, portname=port_name, description=desc, variant=variant, portdir=port_dir,homepage=homepage,platform=platform,cur_version=version,license=license,long_desc=long_description)
		count +=1
		id +=1
		#print("completed the INSERT")
		#print(c.fetchall())

	'''
	b = jsonparser(k)
	port_name = b['name']
	desc = b['description']
	variant = b['variants']
	port_dir = b['portdir']
	c = Port.objects.create(portname=port_name, description=desc, variant=variant, portdir=port_dir)
	'''
	#from django.db import connection
	#to print the query in console
	#data= Port.objects.filter(portname=port_name)
	#print connection.queries[-1]
	
	#return render(request,'port/data.html',{"port1":data.last()})
	return render(request,'port/data.html',{"port1":count})




def find(request):
	if request.method == 'POST':
			port_name = request.POST.get('textfield', None)
			data=Port.objects.filter(portname__icontains=port_name)
			
			return render(request, 'port/portmain.html',{"object_list":data,"flag":1})
	else:
		return render(request,'port/portmain.html')
	
