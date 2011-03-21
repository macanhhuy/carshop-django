# coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from carshop.product.models import *


def customSeatCovers(request, productTypeId, productSubTypeId=None):
	if productSubTypeId:
		print(productTypeId + ' -- ' + productSubTypeId)
	else:
		print(productTypeId)
		
	return render_to_response('product.html', {}, RequestContext(request))
