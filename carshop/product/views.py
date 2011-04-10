# -*- coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from carshop.models import Parameter
from carshop.product.models import *

def allCar(request):
	cars = list(ProductionFor.objects.raw('select pf.id, pf.name from production_for as pf order by pf.name'))
	return render_to_response('allCar.html', {'cars': cars}, RequestContext(request))

	
def findProductTypeById(request, productTypeId):

	type = Parameter.objects.get(id=productTypeId)
	products = Product.objects.extra(where=['product_type_id in (select par.id from parameter as par where par.parameter_parent_id=%s)',], params=[productTypeId,])
		
	return render_to_response('productType.html', {'type': type, 'products':products}, RequestContext(request))

	
def findProductById(request, productTypeId, productSubTypeId=None):
	#from django.db import connection
	#cursor = connection.cursor()
	
	type = Parameter.objects.get(id=productSubTypeId)
	products = Product.objects.extra(where=['product_type_id=%s and exists (select * from parameter as par where par.parameter_parent_id=%s and par.id=%s)',], params=[productSubTypeId, productTypeId, productSubTypeId,])
		
	return render_to_response('product.html', {'type':type, 'products':products}, RequestContext(request))

	
	
def findProductByCarId(request, carId):
	try:
		car = ProductionFor.objects.get(id=carId)
		
		
		return render_to_response('productByCarId.html', {'car': car}, RequestContext(request))
		
	except ProductionFor.DoesNotExist:
		return render_to_response('error.html', {'e': u'don\'t have this car'}, RequestContext(request))
