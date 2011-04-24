# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from carshop.models import Parameter
from carshop.product.models import *

def allCar(request):
	cars = list(Car.objects.raw('select car.id, car.name from car order by car.name'))
	return render_to_response('allCar.html', {'cars': cars}, RequestContext(request))

	
def findProductTypeById(request, productTypeId):

	type = Parameter.objects.get(id=productTypeId)
	products = Product.objects.extra(where=['product_type_id in (select par.id from parameter as par where par.parameter_parent_id=%s)',], params=[productTypeId,])
		
	return render_to_response('productType.html', {'type': type, 'products':products}, RequestContext(request))

	
def findProductById(request, productTypeId, productId):
	#from django.db import connection
	#cursor = connection.cursor()
	
	product = Product.objects.get(id=productId, product_category=productTypeId)
	print(product.product_name)
	return render_to_response('product.html', {'product':product}, RequestContext(request))

	
	
def findProductByCarId(request, carId):
	try:
		car = Car.objects.get(id=carId)
		return render_to_response('productByCarId.html', {'car': car}, RequestContext(request))
		
	except Car.DoesNotExist:
		return render_to_response('error.html', {'e': u'don\'t have this car'}, RequestContext(request))

	
def allProduct(request):
	
	products = Product.objects.all()
	return render_to_response('allProduct.html', {'products': products}, RequestContext(request))
	