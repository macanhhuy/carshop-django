# coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from carshop.system.models import Parameter
from carshop.product.models import *


def customSeatCovers(request, productTypeId, productSubTypeId=None):
	from django.db import connection
	cursor = connection.cursor()
	
	if productSubTypeId:
		products = Product.objects.extra(where=['product_type_id=%s and exists (select * from parameter as par where par.parameter_parent_id=%s and par.id=%s)',], params=[productSubTypeId, productTypeId, productSubTypeId,])
	else:
		products = Product.objects.extra(where=['product_type_id in (select par.id from parameter as par where par.parameter_parent_id=%s)',], params=[productTypeId,])
		
		
	return render_to_response('product.html', {'products':products}, RequestContext(request))
