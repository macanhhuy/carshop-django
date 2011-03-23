# coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from carshop.system.models import Parameter
from carshop.product.models import *


def customSeatCovers(request, productTypeId, productSubTypeId=None):
	from django.db import connection, transaction
	cursor = connection.cursor()
	
	products = []
	if productSubTypeId:
		productSubType = Parameter.objects.filter(id=productSubTypeId, parameter_parent=productTypeId)
		if productSubType:
			cursor.execute("select p.* from product as p where p.product_type_id=%s", [productSubTypeId,])
			products = cursor.fetchone()
		
	else:
		print(productTypeId)
		
		
	return render_to_response('product.html', {'products':products}, RequestContext(request))
