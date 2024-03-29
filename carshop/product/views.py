# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from carshop.models import Parameter
from .models import *




#def findProductTypeById(request, productTypeId):
#    type = Parameter.objects.get(pk=productTypeId)
#    products = Product.objects.extra(
#        where=['product_type_id in (select par.id from parameter as par where par.parameter_parent_id=%s)', ],
#        params=[productTypeId, ])

#    return render_to_response('productType.html', {'type': type, 'products': products}, RequestContext(request))


def findProductById(request, productId):
    #from django.db import connection
    #cursor = connection.cursor()

    product = Product.objects.get(pk=productId)
    return render_to_response('product.html', {'product': product}, RequestContext(request))


def findProductByCarId(request, carId):
    try:
        car = Car.objects.get(pk=carId)
        return render_to_response('productByCarId.html', {'car': car}, RequestContext(request))

    except Car.DoesNotExist:
        return render_to_response('error.html', {'e': u'don\'t have this car'}, RequestContext(request))


def all(request, pageIndex=1):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 8)

    try:
        products = paginator.page(pageIndex)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render_to_response('all.html', {'products': products}, RequestContext(request))

def findCartByMaker(request, manufacturerName):
    pass
    
    
def findProductByName(request, name):
    name = name.replace('-', ' ')
    product = Product.objects.get(product_name=name)
    return render_to_response('product.html', {'product': product}, RequestContext(request))
