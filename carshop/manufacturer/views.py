# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from carshop.manufacturer.models import *

def allManufacturer(request):
	manufacturers = Manufacturer.objects.all()
	
	return render_to_response('allManufacturer.html', RequestContext(request, {'manufacturers': manufacturers}))